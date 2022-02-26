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
from Model.config import Config

items_to_process = list()
items_to_send = list()
dolphin_busy = False
world_id = Config.get_config().get_world_id()
game_room = Config.get_config().get_game_room()
event_scanning = Config.get_config().Scanner_Enabled
disable_multiplayer = Config.get_config().Disable_Multiplayer


async def start_connections(server_config: ServerConfig, set_up_dto: SetUpDto, clientOutput: QListWidget):
    asyncio.create_task(connect_dolphin())
    if not disable_multiplayer:
        await client(server_config)


async def client(server_config: ServerConfig):
    frame_manager = StompFrameManager(server_config)
    try:
        async with websockets.connect("ws://" + server_config.get_uri()) as client_websocket:
            print(f"Attempting to Connect to {game_room}.........")
            await client_websocket.send(frame_manager.connect(server_config.server_ip))
            foo = await client_websocket.recv()
            if not foo.startswith("ERROR"):
                await client_websocket.send(frame_manager.subscribe(f"/topic/item/{game_room}"))
                asyncio.create_task(listen_to_server(client_websocket))
                print(f"Successfully connected to the Server")
                while True:
                    for itemDto in items_to_send:
                        await client_websocket.send(frame_manager.send_json(f"/app/item/{game_room}", json.dumps(itemDto.as_dict())))
                        items_to_send.remove(itemDto)
                    await asyncio.sleep(0)
            else:
                print("Failed to Subscribe to Item Queue, like a bad config.txt")
    except Exception as e:
        print("Problem with Server connection, please check the status with the Server host.")


async def listen_to_server(client_connection):
    async for message in client_connection:
        a = asyncio.create_task(handle_message(message))
        await asyncio.sleep(0)


async def handle_message(message):
    if message[:7] == "MESSAGE":
        contents = message.split("\n")
        item_dto = ItemDto.from_dict(json.loads(contents[-1][:-1]))
        if item_dto.sourcePlayerWorldId != world_id:
            items_to_process.append(item_dto)


async def connect_dolphin():
    while not WWI.is_hooked():
        WWI.hook()
        if WWI.is_hooked():
            break
        await asyncio.sleep(15)
        print("Dolphin was not found, trying again in 15 seconds.")
    await handle_dolphin()


async def handle_dolphin():
    print("Connected To Dolphin")
    while WWI.is_hooked():
        try:
            state = WWI.read_chest_items()
            if state[0] != 0 and state[1] != 0:
                item_dto = ItemDto(world_id, 0, state[1])
                print_item_dto(item_dto)
                items_to_send.append(item_dto)
                WWI.clear_chest_items()
        except RuntimeError as rne:
            del rne
        finally:
            if len(items_to_process) > 0:
                asyncio.create_task(give_item())
        await asyncio.sleep(0)
    print("Disconnected from Dolphin, attempting to reconnect.....")
    asyncio.create_task(connect_dolphin())


async def give_item():
    print_item_dto(items_to_process[0])
    while len(items_to_process) > 0:
        item_dto = items_to_process[-1]
        try:
            if WWI.check_valid_state():
                await asyncio.sleep(3)
                continue
            WWI.give_item_by_value(item_dto.itemId)
            items_to_process.pop()
            await asyncio.sleep(0)
        except Exception as exc:
            print(exc)
            del exc


def print_item_dto(itemDto: ItemDto):
    print(f"{WWR.item_name_dict[itemDto.itemId]} was found in world {itemDto.sourcePlayerWorldId}")
