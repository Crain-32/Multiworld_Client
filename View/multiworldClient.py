import asyncio

from PySide6.QtWidgets import *
from PySide6.QtCore import QThread, QObject, Signal, Slot

from View.uiMultiworldClient import uiMultiworldClient
from Model.serverConfig import ServerConfig
from Model.multiplayerSetUpDto import MultiplayerSetUpDto
from Client.clientCommunication import ClientCommunication

from Model.config import Config


class JoinServerWorker(QObject):
    
    message = Signal(str) # to communicate with parent (gui) thread

    def __init__(self):
        super(JoinServerWorker, self).__init__()
        self.config = Config.get_config()

    def run(self) -> None:
        server_config = ServerConfig(self.config.Server_Address, self.config.Port,
                                     self.config.World_id, self.config.Game_Mode, 'admin', 'adminPass')
        set_up_dto = MultiplayerSetUpDto(self.config.Max_Players, self.config.Game_Room, None, False)
        try:
            clientFunctions = ClientCommunication(self.config, self.message)
            asyncio.run(clientFunctions.start_connections(server_config, set_up_dto))
            
        except RuntimeWarning:
            self.send_message("Failed to Create Room")

    def send_message(self, msg: str) -> None: # to (maybe) receive messages from the actual connection things, haven't gotten that far yet
        self.message.emit(msg)

class MultiworldClientWindow(QMainWindow):

    def __init__(self) -> None:
        super(MultiworldClientWindow, self).__init__()
        self.config = None
        self.ServerJoiner = None
        self.ui = uiMultiworldClient()
        self.ui.setupUi(self)
        self.ui.serverButton.clicked.connect(self.create_room)
        self.ui.joinButton.clicked.connect(self.join_room)
        self.show_button() # Update button to only show the right one of the two to reflect the default value of modeSelector
        self.game_mode_options_toggle()
        self.ui.disconnectButton.clicked.connect(self.disconnect)
        self.ui.disconnectButton.hide()

        self.ui.connectionSelection.currentTextChanged.connect(self.show_button)
        self.ui.modeSelector.currentTextChanged.connect(self.game_mode_options_toggle)
        self.ServerThread = QThread()

        self.load_config()
        self.show()

    @Slot(str)
    def log(self, message: str) -> None:
        self.ui.dialogLog.addItem(message)
        self.ui.dialogLog.scrollToBottom()

    def load_config(self) -> None:
        self.config = Config.get_config()

        self.ui.serverIpInput.setText(self.config.Server_Address)
        self.ui.serverPortInput.setText(str(self.config.Port))
        self.ui.gameRoomNameInput.setText(self.config.Game_Room)
        self.ui.worldIdInput.setText(str(self.config.World_id))
        self.ui.maxPlayersInput.setText(str(self.config.Max_Players))
        if self.config.Game_Mode == "Multiworld":
            self.ui.modeSelector.setCurrentIndex(0)
        else:
            self.ui.modeSelector.setCurrentIndex(1)

    def update_config(self) -> None:
        if self.config.Server_Address != self.ui.serverIpInput.text():
            self.config.Server_Address = self.ui.serverIpInput.text().strip()
        if self.config.Port != int(self.ui.serverPortInput.text()):
            self.config.Port = int(self.ui.serverPortInput.text().strip())
        if self.config.Game_Room != self.ui.gameRoomNameInput.text():
            self.config.Game_Room = self.ui.gameRoomNameInput.text().strip()
        if self.config.World_id != int(self.ui.worldIdInput.text()):
            self.config.World_id = int(self.ui.worldIdInput.text().strip())
        if self.config.Max_Players != int(self.ui.maxPlayersInput.text()):
            self.config.Max_Players = int(self.ui.maxPlayersInput.text().strip())
        if self.config.Game_Mode != self.ui.modeSelector.currentText():
            self.config.Game_Mode = self.ui.modeSelector.currentText().strip()
        if self.config.Player_Name != self.ui.playerName.text():
            self.config.Player_Name = self.ui.playerName.text().strip()

    def create_room(self) -> None:
        pass # TODO actual room setup, needs server-side implementation first

    def join_room(self) -> None:
        self.update_config()

        self.ServerJoiner = JoinServerWorker()
        self.ServerJoiner.moveToThread(self.ServerThread)
        self.ServerThread.started.connect(self.ServerJoiner.run)

        self.ServerJoiner.message.connect(self.log)
        self.ServerThread.start()
        
        self.ui.joinButton.setEnabled(False)
        self.ui.disconnectButton.show()

    def disconnect(self) -> None:
        if self.ServerThread.isRunning():
            self.ServerThread.requestInterruption()
            self.ServerThread.wait()
        self.ui.disconnectButton.hide()
        self.ui.joinButton.setEnabled(True)
        self.ui.serverButton.setEnabled(True)

    def show_button(self) -> None:
        # Used to display the correct button when the Mode Selector dropdown value changes
        mode = self.ui.connectionSelection.currentText()
        if mode == "Join Room":
            self.ui.joinButton.show()
            self.ui.serverButton.hide()
        elif mode == "Set-up Room":
            self.ui.joinButton.hide()
            self.ui.serverButton.show()

    def game_mode_options_toggle(self) -> None:
        # Used to disable "Max Players" and "World Id" when on Coop, and "Player Name" when on Multiworld
        mode = self.ui.modeSelector.currentText()
        if mode == "Multiworld":
            self.ui.worldIdInput.setEnabled(True)
            self.ui.maxPlayersInput.setEnabled(True)
            self.ui.playerName.setEnabled(False)
        elif mode == "Coop":
            self.ui.worldIdInput.setEnabled(False)
            self.ui.maxPlayersInput.setEnabled(False)
            self.ui.playerName.setEnabled(True)


    def closeEvent(self, event) -> None: # Triggers when the user clicks the 'X' to close the window
        self.disconnect()
        event.accept() # Let the window close
