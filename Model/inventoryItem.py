from dataclasses import dataclass

from base_logger import logging
from util.clientExceptions import DuplicateItemWarning

logger = logging.getLogger(__name__)

@dataclass
class InventoryItem:

    item_name: str
    curr_amount: int
    max_amount: int

    def add_item(self):
        if self.curr_amount == self.max_amount:
            logger.info(f"Current Amount: {self.curr_amount} for {self.item_name} - Limit Hit")
            raise DuplicateItemWarning(f"Attempted to bypass max for {self.item_name}")
        self.curr_amount += 1

    def remove_item(self):
        if self.curr_amount == 0:
            return
        self.curr_amount -= 1

    def at_max(self):
        return self.curr_amount == self.max_amount