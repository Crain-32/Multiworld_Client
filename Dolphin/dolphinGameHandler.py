"""
Handles requests to dolphin.
"""
from typing import Dict, List
import Dolphin.windWakerInterface as WWI
from util.abstractGameHandler import AbstractGameHandler
from util.playerInventory import PlayerInventory
from Model.itemDto import ItemDto

from base_logger import logging
logger = logging.getLogger(__name__)

class DolphinGameHandler(AbstractGameHandler):
    def __init__(self, world_id: int, inventory: PlayerInventory):
        self._world_id = world_id
        self._inventory = inventory

    async def connect(self):
        WWI.hook()

    async def is_connected(self) -> bool:
        return WWI.is_hooked()

    async def give_item(self, item_id: int) -> bool:
        try:
            if WWI.is_title_screen():
                return False
            elif not self._inventory.item_maxed(item_id):
                self._inventory.give_item(item_id)
                WWI.give_item_by_value(item_id)
            return True
        except RuntimeError as exc:
            logger.error(exc)
            del exc
            return False

    async def toggle_event(self, event_type: str, event_index: int, enable: bool) -> None:
        pass

    async def get_items(self) -> Dict[int, int]:
        pass

    async def get_queued_items(self) -> ItemDto | None:
        target_world, item_id = WWI.read_chest_items()
        if target_world == 0  and item_id == 0:
            return
        elif target_world != self._world_id and not self._inventory.item_maxed(item_id):
            WWI.remove_item_by_value(item_id)
        elif target_world == self._world_id and not self._inventory.item_maxed(item_id):
            self._inventory.give_item(item_id)
        return ItemDto(sourcePlayerWorldId=self._world_id, targetPlayerWorldId=target_world, itemId=item_id)

    async def clear_queued_items(self):
        WWI.clear_chest_items()
