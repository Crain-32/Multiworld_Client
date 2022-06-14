"""
Handles requests to dolphin.
"""
import functools
from asyncio import Task
from typing import Dict, Union

import Dolphin.windWakerInterface as WWI
from Model.ServerDto.itemDto import ItemDto
from base_logger import logging
from util.abstractGameHandler import AbstractGameHandler
from util.playerInventory import PlayerInventory

logger = logging.getLogger(__name__)


class DolphinGameHandler(AbstractGameHandler):

    def __init__(self, world_id: int, inventory: PlayerInventory):
        logger.debug("Loading Dolphin Game Handler")
        self._world_id = world_id
        self._inventory = inventory
        self.give_item = functools.partial(validate_receivable_item, player_world_id=world_id)
        self.dto_factory = functools.partial(item_dto_wrapper, world_id)

    async def connect(self):
        WWI.hook()

    async def is_connected(self) -> bool:
        return WWI.is_hooked()

    async def pass_item(self, item_id: int) -> bool:
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

    async def get_queued_items(self) -> Union[ItemDto, None]:
        target_world, item_id = WWI.read_chest_items()
        if target_world == 0 and item_id == 0:
            return None
        # If the player should have this item, then we want to track it in the Inventory
        elif self.give_item(item_id, target_world, self._inventory):
            logger.debug(f"Giving {item_id} to {target_world}'s Inventory")
            self._inventory.give_item(item_id)
        return self.dto_factory(item_id, target_world)

    async def clear_queued_items(self):
        WWI.clear_chest_items()

    async def verification_loop(self) -> Task:
        pass


def item_dto_wrapper(source_world: int, item_id: int, target_world: int) -> ItemDto:
    return ItemDto(sourcePlayerWorldId=source_world, targetPlayerWorldId=target_world, itemId=item_id)

def validate_receivable_item(item_id: int, target_world:int, player_inventory: PlayerInventory, player_world_id:int) -> bool:
    return target_world == player_world_id and not player_inventory.item_maxed(item_id)

