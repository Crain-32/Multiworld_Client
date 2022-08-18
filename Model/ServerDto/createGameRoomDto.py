from dataclasses import dataclass, asdict
from typing import AnyStr

from ..config import Config


@dataclass
class CreateGameRoomDto:
    gameRoomName: AnyStr
    playerAmount: int
    worldAmount: int
    gameRoomPassword: AnyStr
    worldType: AnyStr

    def __init__(self, worldAmount: int, playerAmount: int, gameRoomName="GameRoom", gameRoomPassword="password",
                 worldType="MULTIWORLD"):
        self.worldAmount = worldAmount
        self.gameRoomName = gameRoomName
        self.gameRoomPassword = gameRoomPassword
        self.playerAmount = playerAmount
        self.worldType = worldType

    def as_dict(self):
        return asdict(self)

    @classmethod
    def from_client_config(cls, config: Config, password: AnyStr):
        game_mode: AnyStr = "MULTIWORLD"
        if config.Game_Mode.upper() == "COOP":
            game_mode = "COOP"
        return cls(config.Max_Worlds, config.Max_Worlds, config.Game_Room, password, game_mode)
