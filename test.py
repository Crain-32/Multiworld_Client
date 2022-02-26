import asyncio
import json

import websockets

from Client.stompframemanager import StompFrameManager
from Model.itemDto import ItemDto
#from Model.config import Config

address = "twwmultiplayer.com"
port = 8080
world_id = 69
game_room = "Test"


async def test():
    async with websockets.connect(f"ws://{address}:{port}/ws") as websocket:
        f = StompFrameManager(None)
        await websocket.send(f.connect(f"{address}"))
        foo = await websocket.recv()
        print(foo)
        print(websocket.id)
        await websocket.send(f.subscribe(f"/topic/item/{game_room}"))
        print("Subscribed")
        test_dto = ItemDto(world_id, 0, 0x24)
        await websocket.send(f.send_json(f"/app/item/{game_room}", json.dumps(test_dto.as_dict())))
        foo = await websocket.recv()
        print(foo)

asyncio.run(test())
