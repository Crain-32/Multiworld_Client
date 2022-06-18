import asyncio

from PySide6.QtCore import QThread, QObject, Signal, Slot
from PySide6.QtWidgets import *

from Client.clientCommunication import ClientCommunication
from Model.config import Config
from Model.serverConfig import ServerConfig
from View.uiMultiworldClient import Ui_MainWindow
from util.clientExceptions import InvalidPlayerException, InvalidGameRoomException
from util.clientHttpUtil import create_game_room, create_player


class JoinServerWorker(QObject):
    
    message = Signal(str) # to communicate with parent (gui) thread

    def __init__(self):
        super(JoinServerWorker, self).__init__()
        self.config = Config.get_config()

    def run(self) -> None:
        try:
            server_config = ServerConfig(self.config.Server_Address, self.config.Port,
                                         self.config.World_id, self.config.Game_Mode,
                                         self.config.Game_Room, self.config.Player_Name,
                                         self.config.Password)
            clientFunctions = ClientCommunication(self.config, self.message)
            asyncio.run(clientFunctions.start_connections(server_config))
            
        except RuntimeWarning:
            self.send_message("Failed to Create Room")

    def send_message(self, msg: str) -> None: # to (maybe) receive messages from the actual connection things, haven't gotten that far yet
        self.message.emit(msg)

class MultiworldClientWindow(QMainWindow):

    def __init__(self) -> None:
        super(MultiworldClientWindow, self).__init__()
        self.config = None
        self.ServerJoiner = None
        self.ui = Ui_MainWindow()
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
        self.ui.gameRoomNameInput.setText(self.config.Game_Room)
        self.ui.worldInfoInput.setText(str(self.config.World_id))
        if self.config.Game_Mode == "Multiworld":
            self.ui.modeSelector.setCurrentIndex(0)
        else:
            self.ui.modeSelector.setCurrentIndex(1)

    def update_config(self) -> None:
        if self.config.Server_Address != self.ui.serverIpInput.text():
            self.config.Server_Address = self.ui.serverIpInput.text().strip()
        if self.config.Game_Room != self.ui.gameRoomNameInput.text():
            self.config.Game_Room = self.ui.gameRoomNameInput.text().strip()
        if self.ui.connectionSelection.currentText() == "Connect to Room":
            if self.config.World_id != int(self.ui.worldInfoInput.text()):
                self.config.World_id = int(self.ui.worldInfoInput.text().strip())
        else:
            if self.config.Max_Worlds != int(self.ui.worldInfoInput.text()):
                self.config.Max_Worlds = int(self.ui.worldInfoInput.text().strip())
        if self.config.Game_Mode != self.ui.modeSelector.currentText():
            self.config.Game_Mode = self.ui.modeSelector.currentText().strip()
        if self.config.Player_Name != self.ui.playerName.text():
            self.config.Player_Name = self.ui.playerName.text().strip()
        if self.config.Password != self.ui.gameRoomPasswordInput.text():
            self.config.Password = self.ui.gameRoomPasswordInput.text().strip()

    def create_room(self) -> None:
        self.update_config()
        try:
            create_game_room(self.config, self.ui.gameRoomPasswordInput.text())
            self.log(f"{self.config.Game_Room} was successfully created!")
        except InvalidGameRoomException as e:
            self.log(f"Failed to create {self.config.Game_Room}, server returned {e.args}")
            self.log(f"Please use a different Game Room.")

    def join_room(self) -> None:
        self.update_config()
        try:
            player_created = create_player(self.config, self.ui.gameRoomPasswordInput.text())
            if player_created is False:
                self.log(f"A player with the name {self.config.Player_Name} already is connected to {self.config.Game_Room}")
                return None
        except InvalidPlayerException as ipe:
            self.log("".join(ipe.args))
            return None
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
        if mode == "Connect to Room":
            self.ui.joinButton.show()
            self.ui.serverButton.hide()
            self.ui.worldInfoLabel.setText("World ID")
        elif mode == "Create Room":
            self.ui.joinButton.hide()
            self.ui.serverButton.show()
            self.ui.worldInfoLabel.setText("Max Players")

    def game_mode_options_toggle(self) -> None:
        mode = self.ui.modeSelector.currentText()
        if mode == "Multiworld":
            self.ui.worldInfoInput.setEnabled(True)
            self.ui.worldInfoInput.setEnabled(True)
        elif mode == "Coop":
            self.ui.worldInfoInput.setEnabled(False)
            self.ui.worldInfoInput.setEnabled(False)


    def closeEvent(self, event) -> None: # Triggers when the user clicks the 'X' to close the window
        self.disconnect()
        event.accept() # Let the window close
