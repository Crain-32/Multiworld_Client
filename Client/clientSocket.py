"""
Handles Requests/Responses to the Back-end.
"""
import asyncio
import json

import websockets
from PySide6.QtWidgets import QListWidget

import Dolphin.windWakerInterface as WWI
import Dolphin.windWakerResources as WWR
from Client.stompframemanager import StompFrameManager
from Model.itemDto import ItemDto
from Model.serverConfig import ServerConfig
from Model.setUpDto import SetUpDto

items_to_process = list()
items_to_send = list()
dolphin_busy = False
world_id = 0


async def client(server_config: ServerConfig, set_up_dto: SetUpDto, clientOutput: QListWidget):
    world_id = server_config.worldId
    frame_manager = StompFrameManager(server_config)
    print("Trying to Connect to Dolphin......")
    asyncio.create_task(connect_dolphin())
    try:
        async with websockets.connect("ws://" + server_config.get_uri()) as client_websocket:
            print("Connecting to Server.......")
            await client_websocket.send(frame_manager.connect(server_config.server_ip))
            foo = await client_websocket.recv()
            if not foo.startswith("ERROR"):
                print("Subscribing to Item Queue........")
                await client_websocket.send(frame_manager.subscribe("/topic/item"))
                async for message in client_websocket:
                    asyncio.create_task(handle_message(message))
                    await asyncio.sleep(0)
            else:
                print("Failed to Subscribe to Item Queue, please confirm your config with the Server host.")
    except Exception as e:
        print("Problem with Server connection, please check the status with the Server host.")


async def handle_message(message):
    if message[:7] == "MESSAGE":
        contents = message.split("\n")
        item_dto = ItemDto.from_dict(json.loads(contents[-1][:-1]))
        if item_dto.sourcePlayerWorldId != world_id:
            items_to_process.append(item_dto)


async def connect_dolphin():
    while not WWI.is_hooked():
        await asyncio.sleep(1)
        WWI.hook()
    asyncio.create_task(handle_dolphin())


async def handle_dolphin():
    print("Connected to Dolphin.....")
    while WWI.is_hooked():
        await asyncio.sleep(0.5)
        try:
            state = WWI.read_chest_items()
            if state[0] == 1 and state[1] != 0:
                item_dto = ItemDto(world_id, 0, state[1])
                print_item_dto(item_dto)
                items_to_send.append(item_dto)
                WWI.clear_chest_items()
        except RuntimeError as rne:
            del rne
        finally:
            if len(items_to_process) > 0:
                asyncio.create_task(give_item())
    print("Disconnected from Dolphin, attempting to reconnect.....")
    asyncio.create_task(connect_dolphin())


async def give_item():
    while len(items_to_process) > 0:
        item_dto = items_to_process[-1]
        try:
            print("Attempting to Process the Following.....")
            print_item_dto(item_dto)
            WWI.give_item_by_value(item_dto.itemId)
            items_to_process.pop()
            await asyncio.sleep(0)
        except Exception as exc:
            print(exc)
            del exc


def print_item_dto(itemDto: ItemDto):
    print(f"{WWR.item_name_dict[itemDto.itemId]} was found in world {itemDto.sourcePlayerWorldId}")
