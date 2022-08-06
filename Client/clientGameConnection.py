import asyncio
import json
from os import path
from random import Random
from typing import List, Any, Callable
from typing import Union, Coroutine

from PySide6.QtCore import Signal

from Client.types import ItemInfo
from Client.types import PlayerNames
from Dolphin.dolphinGameHandler import DolphinGameHandler
from Model.ServerDto.coopDto import CoopItemDto
from Model.ServerDto.coopDto import output_strs as coop_output_strs
from Model.ServerDto.itemDto import ItemDto
from Model.ServerDto.itemDto import output_strs as multiplayer_output_strs
from Model.config import Config
from View.guiWriter import GuiWriter
from base_logger import logging
from main_paths import DATA_PATH
from util.abstractGameHandler import AbstractGameHandler
from util.clientExceptions import InvalidItemException
from util.playerInventory import PlayerInventory

logger = logging.getLogger(__name__)


class ClientGameConnection(GuiWriter):
    _items_to_process: List[Union[ItemDto, CoopItemDto]] = list()
    _items_to_send: List[Union[ItemDto, CoopItemDto]] = list()
    _world_id: int = 0
    _player_names: PlayerNames = {num: str(num) for num in range(1, 100)}
    _console_handler: AbstractGameHandler
    _write_item_dto: Callable[[Union[ItemDto, CoopItemDto]], Coroutine[Any, Any, None]]

    def __init__(self, world_id: int, signal: Signal = None, config: Config = Config.get_config()):
        logger.info("Loading Client Game Connection")
        super().__init__(signal)
        with open(path.join(DATA_PATH, 'item_information.json')) as item_info_file:
            item_info: ItemInfo = json.load(item_info_file)
        inventory = PlayerInventory()
        inventory.create_inventory(item_info)
        self._console_handler = DolphinGameHandler(world_id, inventory, config.Game_Mode)
        self._world_id = world_id
        self._random = Random()

        self._write_item_dto = self.write_multiplayer_item
        if config.Game_Mode.upper() == "COOP":
            self._write_item_dto = self.write_coop_item

    async def process_items(self) -> None:
        while len(self._items_to_process) > 0:
            item_dto = self._items_to_process[-1]
            await self._write_item_dto(item_dto)
            try:
                if not await self._console_handler.give_item(item_dto.itemId):
                    await asyncio.sleep(4)
                    continue
                self._items_to_process.pop()
                await asyncio.sleep(.25)
            except RuntimeError as exc:
                logger.error(exc)
                del exc

    async def handle(self) -> None:
        await self.write("Connected to Dolphin")
        while await self._console_handler.is_connected():  # Thread set interval instead of a while loop would be better
            try:
                item_dto = await self._console_handler.get_queued_items()
                if item_dto is not None:
                    await self._console_handler.clear_queued_items()
                    await self._write_item_dto(item_dto)
                    self._items_to_send.append(item_dto)

            except RuntimeError as rne:
                logger.info(rne.args)
                del rne
            except InvalidItemException as e:
                logger.info(e.args)
                await self.write(str(e))
            finally:
                if len(self._items_to_process) > 0:
                    asyncio.create_task(self.process_items())
            await asyncio.sleep(.5)
        await self.write("Unexpected Disconnect from Dolphin, attempting to reconnect.....")

    async def connect(self) -> asyncio.Task:
        await self.write("Connecting to Console")
        while not await self._console_handler.is_connected():
            await self._console_handler.connect()
            if await self._console_handler.is_connected():
                break
            await asyncio.sleep(15)
            await self.write("Dolphin was not found, trying again in 15 seconds.")
        return asyncio.create_task(self.handle())

    def set_player_names(self, player_id: int, player_name: str):
        self._player_names[player_id] = player_name

    def get_item_to_send(self) -> List[Union[ItemDto, CoopItemDto]]:
        return self._items_to_send

    def remove_item_to_send(self, item_dto: Union[ItemDto, CoopItemDto]):
        self._items_to_send.remove(item_dto)

    def push_item_to_process(self, item_dto: Union[ItemDto, CoopItemDto]) -> None:
        self._items_to_process.append(item_dto)

    async def write_coop_item(self, item_dto: CoopItemDto) -> None:
        chosen_str = self._random.choice(coop_output_strs)
        await self.write(item_dto.make_output_str(chosen_str))

    async def write_multiplayer_item(self, item_dto: ItemDto) -> None:
        chosen_str = self._random.choice(multiplayer_output_strs)
        await self.write(item_dto.make_output_str(chosen_str, self._player_names))
