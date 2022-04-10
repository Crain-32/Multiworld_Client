from dataclasses import dataclass
from util.clientExceptions import DuplicateItemWarning

@dataclass
class InventoryItem:

    item_name: str
    curr_amount: int
    max_amount: int

    def add_item(self):
        if self.curr_amount == self.max_amount:
            raise DuplicateItemWarning(f"Attempted to bypass max for {self.item_name}")
        self.curr_amount += 1

    def remove_item(self):
        if self.curr_amount == 0:
            return
        self.curr_amount -= 1

    def at_max(self):
        return self.curr_amount == self.max_amount