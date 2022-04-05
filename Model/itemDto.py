from dataclasses import dataclass, asdict
import Dolphin.windWakerResources as WWR

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
    
    def get_simple_output(self) -> str:
        return f"{WWR.item_name_dict[self.itemId]} was found in World {self.sourcePlayerWorldId}"
