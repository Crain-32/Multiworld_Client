from PySide6.QtWidgets import *

from View.uiMultiworldClient import uiMultiworldClient
from Model.serverConfig import ServerConfig
from Model.setUpDto import SetUpDto
from Client.windWakerListener import WindWakerListener


class MultiworldClientWindow(QMainWindow):

    def __init__(self):
        super(MultiworldClientWindow, self).__init__()
        self.ui = uiMultiworldClient()
        self.ui.setupUi(self)
        self.ui.serverButton.clicked.connect(self.create_room)
        self.show()

    def create_room(self):
        server_config = ServerConfig(self.ui.serverIpInput.text().strip(), self.ui.serverPortInput.text().strip(),
                                     int(self.ui.worldIdInput.text()), 'admin', 'adminPass')
        set_up_dto = SetUpDto(int(self.ui.maxPlayersInput.text()), self.ui.gameRoomNameInput.text(), None, False)
        try:
            WindWakerListener(server_config, set_up_dto, self.ui.dialogLog)
            print(server_config.as_dict())
            self.ui.dialogLog.addItem("Room Created with the Name ")
        except RuntimeWarning:
            self.ui.dialogLog.addItem("Failed to Create Room")
