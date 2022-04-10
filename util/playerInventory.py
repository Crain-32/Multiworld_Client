from dataclasses import dataclass
from typing import List, Dict

from Client.clientGameConnection import ItemInfo
from Model.inventoryItem import InventoryItem
from util.clientExceptions import InvalidItemException


@dataclass
class PlayerInventory:
    item_id_item_name_dict: Dict[int, str]
    item_name_inventory_item_dict: Dict[str, InventoryItem]

    def __init__(self):
        self.item_name_inventory_item_dict = dict()
        self.item_id_item_name_dict = dict()

    def create_inventory(self, base_inventory: ItemInfo):
        progressive_items = list(filter((lambda prog: list(prog.keys())[0].startswith("Progressive")), base_inventory))
        other_items = list(filter((lambda other: not list(other.keys())[0].startswith("Progressive")), base_inventory))
        junk_item_ids = list(range(1, 255))
        for item in progressive_items:
            for name_str, info in item.items():
                for item_id in info["item_ids"]:
                    junk_item_ids.remove(item_id)
                    self.item_id_item_name_dict[item_id] = name_str
                inventory_item = InventoryItem(item_name=name_str, curr_amount=0, max_amount=info["max_amount"])
                self.item_name_inventory_item_dict[name_str] = inventory_item
        for item in other_items:
            for name_str, info in item.items():
                junk_item_ids.remove(info["item_id"])
                self.item_id_item_name_dict[info["item_id"]] = name_str
                inventory_item = InventoryItem(item_name=name_str, curr_amount=0, max_amount=info["max_amount"])
                self.item_name_inventory_item_dict[name_str] = inventory_item
        for junk_id in junk_item_ids:
            self.item_id_item_name_dict[junk_id] = "Junk"
        inventory_item = InventoryItem(item_name="Junk", curr_amount=0, max_amount=-1)
        self.item_name_inventory_item_dict["Junk"] = inventory_item

    def set_starting_items(self, starting_item_ids: list[int]) -> None:
        for item_id in starting_item_ids:
            self.give_item(item_id)

    def give_item(self, item_id: int) -> None:
        self.item_id_check(item_id)
        item_name = self.item_id_item_name_dict[item_id]
        self.item_name_inventory_item_dict[item_name].add_item()

    def take_item(self, item_id: int) -> None:
        self.item_id_check(item_id)
        item_name = self.item_id_item_name_dict[item_id]
        self.item_name_inventory_item_dict[item_name].remove_item()

    def item_maxed(self, item_id: int) -> bool:
        self.item_id_check(item_id)
        item_name = self.item_id_item_name_dict[item_id]
        return self.item_name_inventory_item_dict[item_name].at_max()

    def item_id_check(self, item_id: int) -> None:
        if item_id not in self.item_id_item_name_dict:
            raise InvalidItemException(f"Invalid Item ID of {item_id} provided!")
