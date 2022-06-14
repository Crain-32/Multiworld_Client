from dataclasses import dataclass, asdict

import Dolphin.windWakerResources as WWR
from Client.types import PlayerNames

output_strs =  ["World {source} found World {target}'s {item}!",
                "{item} was found by World {source} for World {target}!",
                "World {target}'s {item} was found by World {source}!"]

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
    
    def make_output_str(self, output_str: str, playerNames: PlayerNames) -> str:
        return output_str.format(source=playerNames[self.sourcePlayerWorldId], target=playerNames[self.targetPlayerWorldId], item=WWR.item_name_dict[self.itemId])
