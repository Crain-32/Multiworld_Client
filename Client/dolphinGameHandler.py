"""
Handles requests to dolphin.
"""
import asyncio
from asyncio import Task

from typing import Dict, List
import Dolphin.windWakerInterface as WWI

from Client.abstractGameHandler import AbstractGameHandler
from Model.itemDto import ItemDto


class DolphinGameHandler(AbstractGameHandler):
    _items_to_process: List[ItemDto] = list() # This needs to hook back into the client somehow
    _items_to_send: List[ItemDto] = list()  # This needs to hook back into the client somehow
    _world_id: int = 0

    def __init__(self, world_id: int):
        _world_id = world_id

    def is_connected(self) -> bool:
        return WWI.is_hooked()

    def give_item(self, item_id: int) -> bool:
        try:
            if WWI.is_title_screen():
                return False
            WWI.give_item_by_value(item_id)
            return True
        except RuntimeError as exc:
            print(exc)
            del exc
            return False

    def toggle_event(self, event_type: str, event_index: int, enable: bool) -> None:
        pass

    def get_items(self) -> Dict[int, int]:
        pass

    async def process_items(self) -> None:
        while len(self._items_to_process) > 0:
            item_dto = self._items_to_process[-1]
            print_item_dto(item_dto)
            try:
                if not self.give_item(item_dto.itemId):
                    await asyncio.sleep(3)
                    continue
                self._items_to_process.pop()
                await asyncio.sleep(0)
            except RuntimeError as exc:
                print(exc)
                del exc

    async def handle_dolphin(self) -> None:
        print("Connected To Dolphin")
        while WWI.is_hooked():  # Thread set interval instead of a while loop would be better
            try:
                state = WWI.read_chest_items()
                if state[0] != 0 and state[1] != 0 and state[1] != 0xFF:
                    item_dto = ItemDto(self._world_id, 0, state[1])  # World ID should be set in client
                    print_item_dto(item_dto)
                    self._items_to_send.append(item_dto)
                    WWI.clear_chest_items()
            except RuntimeError as rne:
                del rne
            finally:
                if len(self._items_to_process) > 0:
                    asyncio.create_task(self.process_items())
            await asyncio.sleep(0)
        print("Disconnected from Dolphin, attempting to reconnect.....")

    def get_item_to_send(self) -> List[ItemDto]:
        return self._items_to_send

    def remove_item_to_send(self, item_dto:ItemDto):
        self._items_to_send.remove(item_dto)

    def push_item_to_process(self, item_dto: ItemDto) -> None:
        self._items_to_process.append(item_dto)

    async def connect_dolphin(self) -> Task:
        print("Connecting to Dolphin")
        while not WWI.is_hooked():
            WWI.hook()
            if WWI.is_hooked():
                break
            await asyncio.sleep(15)
            print("Dolphin was not found, trying again in 15 seconds.")
        return asyncio.create_task(self.handle_dolphin())


def print_item_dto(itemDto: ItemDto) -> None:
    print(f"{WWR.item_name_dict[itemDto.itemId]} was found in world {itemDto.sourcePlayerWorldId}")