import asyncio

from PySide6.QtWidgets import *
from PySide6.QtCore import QThread, QObject, Signal, Slot

from View.uiMultiworldClient import uiMultiworldClient
from Model.serverConfig import ServerConfig
from Model.setUpDto import SetUpDto
import Client.clientCommunication as clientFunctions

from Model.config import Config


class ServerWorker(QObject):
    
    message = Signal(str) # to communicate with parent thread

    def __init__(self):
        super(ServerWorker, self).__init__()
        self.config = Config.get_config()


    def run(self):
        print("Setting Fields")
        server_config = ServerConfig(self.config._ServerAddress, self.config._Port,
        self.config._World_id, 'admin', 'adminPass')
        set_up_dto = SetUpDto(1, self.config._Game_Room, None, False) # 1 = world amount, just 1 for testing to match with number assigned to input box
        try:
            print("Into Listener")
            asyncio.run(clientFunctions.start_connections(server_config, set_up_dto, self.send_message))
            
        except RuntimeWarning:
            self.send_message("Failed to Create Room")

    @Slot(str)
    def send_message(self, msg: str): # to (maybe) receive messages from the actual connection things, haven't gotten that far yet
        self.message.emit(msg)

class MultiworldClientWindow(QMainWindow):

    def __init__(self):
        super(MultiworldClientWindow, self).__init__()
        self.ui = uiMultiworldClient()
        self.ui.setupUi(self)
        self.ui.serverButton.clicked.connect(self.create_room)
        self.ui.joinButton.clicked.connect(self.join_room)
        self.show_button() # Update button to only show the right one of the two to reflect the default value of modeSelector
        self.ui.disconnectButton.clicked.connect(self.disconnect)
        self.ui.disconnectButton.hide()

        self.ui.modeSelector.currentTextChanged.connect(self.show_button)

        self.load_config()
        self.show()

    @Slot(str)
    def log(self, message: str):
        self.ui.dialogLog.addItem(message)
        self.ui.dialogLog.scrollToBottom()

    def load_config(self):
        self.config = Config.get_config()

        self.ui.serverIpInput.setText(self.config._ServerAddress)
        self.ui.serverPortInput.setText(str(self.config._Port))
        self.ui.gameRoomNameInput.setText(self.config._Game_Room)
        self.ui.worldIdInput.setText(str(self.config._World_id))
        self.ui.maxPlayersInput.setText("1") #testing

    def update_config(self):
        if self.config._ServerAddress != self.ui.serverIpInput.text():
            self.config._ServerAddress = self.ui.serverIpInput.text().strip()
        if self.config._Port != int(self.ui.serverPortInput.text()):
            self.config._Port = int(self.ui.serverPortInput.text().strip())
        if self.config._Game_Room != self.ui.gameRoomNameInput.text():
            self.config._Game_Room = self.ui.gameRoomNameInput.text().strip()
        if self.config._World_id != int(self.ui.worldIdInput.text()):
            self.config._World_id = int(self.ui.worldIdInput.text().strip())

    def create_room(self):
        self.update_config()

        self.ServerThread = QThread()
        self.ServerMaker = ServerWorker()
        self.ServerMaker.moveToThread(self.ServerThread)
        self.ServerThread.started.connect(self.ServerMaker.run)
        

        self.ServerMaker.message.connect(self.log)
        self.ServerThread.start()
        
        self.ui.serverButton.setEnabled(False)
        self.ui.disconnectButton.show()

    def join_room(self):
        pass # TODO joining room stuff

    def disconnect(self):
        pass # TODO proper thread ending and server disconnect

    def show_button(self):
        # Used to display the correct button when the Mode Selector dropdown value changes
        mode = self.ui.modeSelector.currentText()
        if mode == "Connect to Room":
            self.ui.joinButton.show()
            self.ui.serverButton.hide()
        elif mode == "Set-up Room":
            self.ui.joinButton.hide()
            self.ui.serverButton.show()
