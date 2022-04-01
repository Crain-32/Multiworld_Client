import asyncio
from asyncio import Task
from typing import List

from Dolphin.dolphinGameHandler import DolphinGameHandler
from Model.itemDto import ItemDto
from util.abstractGameHandler import AbstractGameHandler
import Dolphin.windWakerResources as WWR

from PySide6.QtCore import Signal


class ClientGameConnection:
    _items_to_process: List[ItemDto] = list()
    _items_to_send: List[ItemDto] = list()
    _world_id: int = 0

    _console_handler: AbstractGameHandler

    gui_logger_signal: Signal

    def __init__(self, world_id: int):
        self._console_handler = DolphinGameHandler(world_id)

    async def process_items(self) -> None:
        while len(self._items_to_process) > 0:
            item_dto = self._items_to_process[-1]
            await self.print_item_dto(item_dto)
            try:
                if not await self._console_handler.give_item(item_dto.itemId):
                    await asyncio.sleep(3)
                    continue
                self._items_to_process.pop()
                await asyncio.sleep(0)
            except RuntimeError as exc:
                print(exc)
                del exc

    async def handle(self) -> None:
        await self.log("Connected To Console")
        while await self._console_handler.is_connected():  # Thread set interval instead of a while loop would be better
            try:
                state = await self._console_handler.get_queued_items()
                if state[0] != 0 and state[1] != 0 and state[1] != 0xFF:
                    item_dto = ItemDto(self._world_id, 0, state[1])  # World ID should be set in client
                    await self.print_item_dto(item_dto)
                    self._items_to_send.append(item_dto)
                    await self._console_handler.clear_queued_items()
            except RuntimeError as rne:
                del rne
            finally:
                if len(self._items_to_process) > 0:
                    asyncio.create_task(self.process_items())
            await asyncio.sleep(0)
        await self.log("Disconnected from Console, attempting to reconnect.....")

    async def connect(self, gui_logger_signal: Signal) -> Task:
        self.gui_logger_signal = gui_logger_signal
        await self.log("Connecting to Console")
        while not await self._console_handler.is_connected():
            await self._console_handler.connect()
            if await self._console_handler.is_connected():
                break
            await asyncio.sleep(15)
            await self.log("Console was not found, trying again in 15 seconds.")
        return asyncio.create_task(self.handle())

    async def log(self, message: str) -> None:
        assert isinstance(self.gui_logger_signal, Signal)
        self.gui_logger_signal.emit(message)

    def get_item_to_send(self) -> List[ItemDto]:
        return self._items_to_send

    def remove_item_to_send(self, item_dto:ItemDto):
        self._items_to_send.remove(item_dto)

    def push_item_to_process(self, item_dto: ItemDto) -> None:
        self._items_to_process.append(item_dto)
    
    async def print_item_dto(self, itemDto: ItemDto) -> None:
        await self.log(f"{WWR.item_name_dict[itemDto.itemId]} was found in world {itemDto.sourcePlayerWorldId}")
