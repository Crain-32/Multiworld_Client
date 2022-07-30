"""
Handles Communication with Dolphin.
"""
import functools
from asyncio import Task
from typing import Dict, Union, AnyStr, Generator

import Dolphin.windWakerInterface as WWI
from Client.types import EventInfo
from Model.ServerDto.coopDto import CoopItemDto
from Model.ServerDto.itemDto import ItemDto
from Model.config import Config
from base_logger import logging
from util.abstractGameHandler import AbstractGameHandler
from util.playerInventory import PlayerInventory

logger = logging.getLogger(__name__)


class DolphinGameHandler(AbstractGameHandler):

    def __init__(self, world_id: int, inventory: PlayerInventory, game_mode: AnyStr):
        logger.debug("Loading Dolphin Game Handler")
        config: Config = Config.get_config()
        self._world_id = world_id
        self._inventory = inventory
        self._game_mode = game_mode
        self.give_item = functools.partial(validate_receivable_item, player_world_id=world_id)
        if game_mode == "COOP":
            self.dto_factory = functools.partial(coop_dto_wrapper, source_player=config.Player_Name)
        else:
            self.dto_factory = functools.partial(item_dto_wrapper, world_id)

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

    async def watch_events(self) -> Generator[EventInfo, None, None]:
        pass

    async def get_items(self) -> Dict[int, int]:
        pass

    async def get_queued_items(self) -> Union[ItemDto, CoopItemDto, None]:
        target_world, item_id = WWI.read_chest_items()
        if self._game_mode == "COOP" and WWI.coop_item_filter(item_id):
            return None

        elif not (target_world and item_id):
            return None

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


def coop_dto_wrapper(source_player: AnyStr, item_id: int, *args) -> CoopItemDto:
    return CoopItemDto(sourcePlayer=source_player, itemId=item_id)


def validate_receivable_item(item_id: int, target_world: int, player_inventory: PlayerInventory,
                             player_world_id: int) -> bool:
    return target_world == player_world_id and not player_inventory.item_maxed(item_id)
