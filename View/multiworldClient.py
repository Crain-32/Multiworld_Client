import asyncio

from PySide6.QtWidgets import *
from PySide6.QtCore import QThread, QObject, Signal, Slot

from View.uiMultiworldClient import uiMultiworldClient
from Model.serverConfig import ServerConfig
from Model.setUpDto import SetUpDto
import Client.clientCommunication as clientFunctions

from Model.config import Config


class JoinServerWorker(QObject):
    
    message = Signal(str) # to communicate with parent (gui) thread

    def __init__(self):
        super(JoinServerWorker, self).__init__()
        self.config = Config.get_config()


    def run(self) -> None:
        print("Setting Fields")
        server_config = ServerConfig(self.config._ServerAddress, self.config._Port,
        self.config._World_id, 'admin', 'adminPass')
        set_up_dto = SetUpDto(self.config._Max_Players, self.config._Game_Room, None, False)
        try:
            print("Into Listener")
            asyncio.run(clientFunctions.start_connections(server_config, set_up_dto, self.message))
            
        except RuntimeWarning:
            self.send_message("Failed to Create Room")

    def send_message(self, msg: str) -> None: # to (maybe) receive messages from the actual connection things, haven't gotten that far yet
        self.message.emit(msg)

class MultiworldClientWindow(QMainWindow):

    def __init__(self) -> None:
        super(MultiworldClientWindow, self).__init__()
        self.ui = uiMultiworldClient()
        self.ui.setupUi(self)
        self.ui.serverButton.clicked.connect(self.create_room)
        self.ui.joinButton.clicked.connect(self.join_room)
        self.show_button() # Update button to only show the right one of the two to reflect the default value of modeSelector
        self.ui.disconnectButton.clicked.connect(self.disconnect)
        self.ui.disconnectButton.hide()

        self.ui.modeSelector.currentTextChanged.connect(self.show_button)

        self.ServerThread = QThread()

        self.load_config()
        self.show()

    @Slot(str)
    def log(self, message: str) -> None:
        self.ui.dialogLog.addItem(message)
        self.ui.dialogLog.scrollToBottom()

    def load_config(self) -> None:
        self.config = Config.get_config()

        self.ui.serverIpInput.setText(self.config._ServerAddress)
        self.ui.serverPortInput.setText(str(self.config._Port))
        self.ui.gameRoomNameInput.setText(self.config._Game_Room)
        self.ui.worldIdInput.setText(str(self.config._World_id))
        self.ui.maxPlayersInput.setText(str(self.config._Max_Players))

    def update_config(self) -> None:
        if self.config._ServerAddress != self.ui.serverIpInput.text():
            self.config._ServerAddress = self.ui.serverIpInput.text().strip()
        if self.config._Port != int(self.ui.serverPortInput.text()):
            self.config._Port = int(self.ui.serverPortInput.text().strip())
        if self.config._Game_Room != self.ui.gameRoomNameInput.text():
            self.config._Game_Room = self.ui.gameRoomNameInput.text().strip()
        if self.config._World_id != int(self.ui.worldIdInput.text()):
            self.config._World_id = int(self.ui.worldIdInput.text().strip())
        if self.config._Max_Players != int(self.ui.maxPlayersInput.text()):
            self.config_Max_Players = int(self.ui.maxPlayersInput.text().strip())

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
        mode = self.ui.modeSelector.currentText()
        if mode == "Connect to Room":
            self.ui.joinButton.show()
            self.ui.serverButton.hide()
        elif mode == "Set-up Room":
            self.ui.joinButton.hide()
            self.ui.serverButton.show()

    def closeEvent(self, event) -> None: # Triggers when the user clicks the 'X' to close the window
        self.disconnect()
        event.accept() # Let the window close