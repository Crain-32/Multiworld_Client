from dataclasses import dataclass, asdict


@dataclass
class ItemDto:
    sourcePlayerWorldId: int
    targetPlayerWorldId: int
    itemId: int

    @staticmethod
    def from_dict(dictionary):
        return ItemDto(dictionary['sourcePlayerWorldId'],
                       dictionary['targetPlayerWorldId'],
                       dictionary['itemId'])

    def __init__(self, sourcePlayerWorldId: int, targetPlayerWorldId: int, itemId: int):
        self.sourcePlayerWorldId = sourcePlayerWorldId
        self.targetPlayerWorldId = targetPlayerWorldId
        self.itemId = itemId

    def as_dict(self):
        return asdict(self)
