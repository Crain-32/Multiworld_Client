from dataclasses import dataclass, asdict
from .itemDto import ItemDto


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
