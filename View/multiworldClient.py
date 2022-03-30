import asyncio

from PySide6.QtWidgets import *

from View.uiMultiworldClient import uiMultiworldClient
from Model.serverConfig import ServerConfig
from Model.setUpDto import SetUpDto
import Client.clientCommunication as clientFunctions


class MultiworldClientWindow(QMainWindow):

    def __init__(self):
        super(MultiworldClientWindow, self).__init__()
        self.ui = uiMultiworldClient()
        self.ui.setupUi(self)
        self.ui.serverButton.clicked.connect(self.create_room)
        self.ui.joinButton.clicked.connect(self.join_room)
        self.ui.serverButton.hide() # By default the option is set to join, not setup
        self.ui.disconnectButton.clicked.connect(self.disconnect)
        self.ui.disconnectButton.hide()

        self.show()

    def create_room(self):
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
