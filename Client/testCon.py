import asyncio
import json

import websockets

from Client.stompframemanager import StompFrameManager
from Model.itemDto import ItemDto
from Model.config import Config

address = Config.get_config().get_address()
port = Config.get_config().get_port()
world_id = Config.get_config().get_world_id()


async def test():
    async with websockets.connect(f"ws://{address}:{port}/ws") as websocket:
        f = StompFrameManager(None)
        await websocket.send(f.connect(f"{address}"))
        foo = await websocket.recv()
        print(foo)
        print(websocket.id)
        await websocket.send(f.subscribe("/topic/item"))
        test_dto = ItemDto(world_id, 0, 0x50)
        await websocket.send(f.send_json("/app/item", json.dumps(test_dto.as_dict())))
        foo = await websocket.recv()
        print(foo)


asyncio.run(test())
