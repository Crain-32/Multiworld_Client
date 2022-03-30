import asyncio

from PySide6.QtWidgets import *

from View.uiMultiworldClient import uiMultiworldClient
from Model.serverConfig import ServerConfig
from Model.setUpDto import SetUpDto
import Client.clientCommunication as clientFunctions

from Model.config import Config


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
        print("Setting Fields")
        server_config = ServerConfig(self.ui.serverIpInput.text().strip(), int(self.ui.serverPortInput.text().strip()),
                                     int(self.ui.worldIdInput.text()), 'admin', 'adminPass')
        set_up_dto = SetUpDto(int(self.ui.maxPlayersInput.text()), self.ui.gameRoomNameInput.text(), None, False)
        try:
            print("Into Listener")
            asyncio.run(clientFunctions.start_connections(server_config, set_up_dto, self.ui.dialogLog))
        except RuntimeWarning:
            self.ui.dialogLog.addItem("Failed to Create Room")

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
