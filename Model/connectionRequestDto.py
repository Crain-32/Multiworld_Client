from dataclasses import dataclass, asdict
from .playerDto import PlayerDto


@dataclass
class ConnectionRequestDto:
    playerDto: PlayerDto
    gameRoomName: str
    gameRoomPassword: str

    def __init__(self, gameRoomName, gameRoomPassword, playerDto):
        self.gameRoomName = gameRoomName
        self.gameRoomPassword = gameRoomPassword
        self.playerDto = playerDto

    def as_dict(self):
        return asdict(self)
