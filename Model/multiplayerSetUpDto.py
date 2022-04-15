from dataclasses import dataclass, asdict


@dataclass
class MultiplayerSetUpDto:
    worldAmount: int
    gameRoomName: str
    gameRoomPassword: str
    extraValidation: bool

    def __init__(self, worldAmount, gameRoomName="", gameRoomPassword="", extraValidation=False):
        self.worldAmount = worldAmount
        self.gameRoomName = gameRoomName
        self.gameRoomPassword = gameRoomPassword
        self.extraValidation = extraValidation

    def as_dict(self):
        return asdict(self)
