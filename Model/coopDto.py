from dataclasses import dataclass, asdict
import Dolphin.windWakerResources as WWR


@dataclass
class CoopDto:
    sourcePlayerName: str
    itemId: int

    @staticmethod
    def from_dict(dictionary):
        return CoopDto(dictionary['sourcePlayerName'],
                             dictionary['itemId'])

    def __init__(self, sourcePlayerName: str, itemId: int):
        self.sourcePlayerName = sourcePlayerName
        self.itemId = itemId

    def as_dict(self):
        return asdict(self)

    def make_output_str(self, *args) -> str:
        return f"{self.sourcePlayerName} found the {WWR.item_name_dict[self.itemId]}"