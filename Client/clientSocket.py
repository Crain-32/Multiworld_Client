"""
Handles Requests/Responses to the Back-end.
"""
import asyncio
import json

import websockets
from PySide6.QtWidgets import QListWidget

import Dolphin.windWakerInterface as WWI
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
    frameManager = StompFrameManager(server_config)
    asyncio.create_task(connect_dolphin())
    async with websockets.connect("ws://" + server_config.get_uri()) as client_websocket:
        print("Upgrade to Websocket was Successful")
        await client_websocket.send(frameManager.connect(server_config.server_ip))
        foo = await client_websocket.recv()
        if foo[0:5] != "ERROR":
            print("Connection to Server was Successful")
            await client_websocket.send(frameManager.subscribe("/topic/test"))
            async for message in client_websocket:
                asyncio.create_task(handle_message(message))
                await asyncio.sleep(0)
    print("Disconnected from Server")


async def handle_message(message):
    if message[:7] == "MESSAGE":
        contents = message.split("\n")
        print("Received from Server: " + contents[-1])
        item_dto = ItemDto.from_dict(json.loads(contents[-1][:-1]))
        if item_dto.targetPlayerWorldId == world_id:
            items_to_process.append(item_dto)


async def connect_dolphin():
    while not WWI.is_hooked():
        await asyncio.sleep(1)
        WWI.hook()
    asyncio.create_task(handle_dolphin())


async def handle_dolphin():
    print("Connected to Dolphin")
    while WWI.is_hooked():
        await asyncio.sleep(0.5)
        try:
            state = WWI.read_chest_items()
            if state[0] != world_id and state[1] != 0:
                item_dto = ItemDto(world_id, state[0], state[1])
                print(f"{state[0]} was found for {state[1]} in world {world_id}")
                items_to_send.append(item_dto)
                WWI.clear_chest_items()
        except RuntimeError as rne:
            del rne
        finally:
            if len(items_to_process) > 0:
                print("Processing Items")
                for key, val in items_to_process[0].as_dict().items():
                    print(key + " : " + str(val))
                WWI.give_item_by_value(items_to_process.pop().itemId)
    print("Disconnected from Dolphin, attempting to reconnect.....")
    asyncio.create_task(connect_dolphin())
