from dataclasses import dataclass, asdict
from typing import AnyStr

from Dolphin.windWakerResources import item_name_dict

output_strs = ["{source} found {item}!",
               "{item} was found by {source}!"]


@dataclass
class CoopItemDto:
    sourcePlayer: str
    itemId: int

    @staticmethod
    def from_dict(dictionary):
        return CoopItemDto(dictionary['sourcePlayer'],
                           dictionary['itemId'])

    def as_dict(self):
        return asdict(self)

    def make_output_str(self, output_str: AnyStr) -> AnyStr:
        return output_str.format(source=self.sourcePlayer, item=item_name_dict[self.itemId])
