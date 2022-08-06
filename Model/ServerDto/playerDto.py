from dataclasses import dataclass, asdict
from typing import Dict, AnyStr

from Model.config import Config


@dataclass
class PlayerDto:
    # id : int | The Client can't send this, but the Server can return it
    playerName: AnyStr
    worldId: int
    worldType: AnyStr
    connected: bool # The Client can't send this, but the Server can return it

    def __init__(self, playerName: AnyStr, worldId: int = 0, worldType: AnyStr = "SHARED", connected: bool = False):
        self.worldId = worldId
        self.playerName = playerName
        self.worldType = worldType
        self.connected  = connected

    @staticmethod
    def from_dict(dic: Dict[AnyStr, AnyStr | int]):
        return PlayerDto(dic['playerName'], dic['worldId'], dic['worldType'], dic['connected'])

    def as_dict(self):
        player_dict: Dict = asdict(self)
        del player_dict["connected"]
        return player_dict

    @staticmethod
    def from_config(config: Config):               #Default to Shared Type since it can handle anything
        return PlayerDto(config.Player_Name, config.World_id, config.Game_Mode.upper())
