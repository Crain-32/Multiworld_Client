"""
Handles requests to dolphin.
"""
import asyncio
from asyncio import Task

from typing import Dict, List
import Dolphin.windWakerInterface as WWI

from Client.abstractGameHandler import AbstractGameHandler


class DolphinGameHandler(AbstractGameHandler):
    def __init__(self, world_id: int):
        _world_id = world_id

    async def connect(self):
        WWI.hook()

    async def is_connected(self) -> bool:
        return WWI.is_hooked()

    async def give_item(self, item_id: int) -> bool:
        try:
            if WWI.is_title_screen():
                return False
            WWI.give_item_by_value(item_id)
            return True
        except RuntimeError as exc:
            print(exc)
            del exc
            return False

    async def toggle_event(self, event_type: str, event_index: int, enable: bool) -> None:
        pass

    async def get_items(self) -> Dict[int, int]:
        pass

    async def get_queued_items(self) -> List[int]:
        return WWI.read_chest_items()

    async def clear_queued_items(self):
        WWI.clear_chest_items()
