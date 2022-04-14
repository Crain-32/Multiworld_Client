import asyncio
import json

import websockets

from util.stompframemanager import StompFrameManager
from Model.multiworldDto import MultiworldDto
from Model.coopDto import CoopDto
#from Model.config import Config

address = "twwmultiplayer.com"
port = 8080
world_id = 4
game_room = "Crain"

async def test():
    async with websockets.connect(f"ws://{address}:{port}/ws") as websocket:
        f = StompFrameManager(None)
        await websocket.send(f.connect(f"{address}"))
        foo = await websocket.recv()
        print(foo)
        print(websocket.id)
        await websocket.send(f.subscribe(f"/topic/multiworld/{game_room}"))
        print("Subscribed")
        test_dto = MultiworldDto(world_id, 1, 167)
        # test_dto = CoopDto("Foobar", 0x34)
        await websocket.send(f.send_json(f"/app/multiworld/{game_room}", json.dumps(test_dto.as_dict())))
        async for message in websocket:
            print(message)

asyncio.run(test())
