from dataclasses import dataclass, asdict
from typing import AnyStr

from ..config import Config


@dataclass
class CreateGameRoomDto:
    gameRoomName: str
    playerAmount: int
    worldAmount: int
    gameRoomPassword: str

    def __init__(self, worldAmount: int, playerAmount: int, gameRoomName="GameRoom", gameRoomPassword="password"):
        self.worldAmount = worldAmount
        self.gameRoomName = gameRoomName
        self.gameRoomPassword = gameRoomPassword
        self.playerAmount = playerAmount

    def as_dict(self):
        return asdict(self)

    @classmethod
    def from_client_config(cls, config: Config, password: AnyStr):
        return cls(config.Max_Worlds, config.Max_Worlds, config.Game_Room, password)