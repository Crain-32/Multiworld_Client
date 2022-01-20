import asyncio
import json

import websockets

from Client.stompframemanager import StompFrameManager
from Model.itemDto import ItemDto


async def test():
    async with websockets.connect("ws://localhost:8080/ws") as websocket:
        f = StompFrameManager(None)
        await websocket.send(f.connect("localhost"))
        foo = await websocket.recv()
        print(foo)
        print(websocket.id)
        await websocket.send(f.subscribe("/topic/test"))
        testDto = ItemDto(4, 0, 0x34)
        await websocket.send(f.send_json("/app/test", json.dumps(testDto.as_dict())))
        foo = await websocket.recv()





asyncio.run(test())