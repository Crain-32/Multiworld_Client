from dataclasses import dataclass, asdict
from .multiworldDto import MultiworldDto
from .serverConfig import ServerConfig


@dataclass
class PlayerDto:
    worldId: int
    userName: str
    connected: bool

    def __init__(self, worldId, userName="", connected=False):
        if isinstance(worldId, dict):
            self.from_dict(worldId)
        else:
            self.worldId = worldId
            self.userName = userName
            self.connected = connected

    def from_dict(self, dic):
        self.worldId = dic['worldId']
        self.userName = dic['userName']
        self.connected = dic['connected']

    def as_dict(self):
        return asdict(self)

    @staticmethod
    def from_server_config(serverConfig: ServerConfig):
        return PlayerDto(serverConfig.worldId, serverConfig.userName)