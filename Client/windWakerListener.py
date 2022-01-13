"""
Handles Requests/Responses to the Back-end.
"""

import stomp
from PySide6.QtWidgets import QListWidget

from Model.connectionRequestDto import ConnectionRequestDto
from Model.itemDto import ItemDto
from Model.playerDto import PlayerDto
from Model.serverConfig import ServerConfig
from Model.setUpDto import SetUpDto


class WindWakerListener(stomp.ConnectionListener):

    def __init__(self, server_config: ServerConfig, set_up_dto: SetUpDto,
                 player_dto: PlayerDto, clientOutput: QListWidget):
        self.server_config = server_config
        self.set_up_dto = set_up_dto
        self.player_dto = player_dto
        self.clientOutput = clientOutput
        self.session_id = ""
        self.conn = self.create_connection_info()

    def connect(self):
        self.conn.connect(self.server_config.userName, self.server_config.password, wait=True,
                          headers={'host': '127.0.0.1'})

    def connect_player(self):
        self.conn.subscribe("/ws/ready/queue", self.session_id)
        connection_request_dto = ConnectionRequestDto(self.set_up_dto.gameRoomName, self.set_up_dto.gameRoomPassword,
                                                      self.player_dto)
        self.conn.send("/ws/ready", connection_request_dto)

    def send_item(self, itemDto: ItemDto):
        self.conn.send("/ws/item/" + self.set_up_dto.gameRoomName, itemDto)

    def create_connection_info(self):
        conn = stomp.Connection([self.server_config.server_ip, self.server_config.server_port])
        conn.set_listener('', self)
        return conn

    def on_connected(self, frame):
        self.session_id = frame.body['session']
        self.clientOutput.addItem("{} successfully joined {}"
                                  .format(self.player_dto.userName, self.set_up_dto.gameRoomName))

    def on_error(self, frame):
        print('received an error "%s"' % frame.body)

    def on_message(self, frame):
        if frame.headers['destination'] == "ws/ready/queue":
            if len(frame.body) == 0:
                self.clientOutput.addItem("Server Refused connection. Double check your Connection Information.")
            else:
                self.conn.subscribe("/ws/queue/gameroom/" + frame.body)

    def on_disconnected(self):
        self.connect()
