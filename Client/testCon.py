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
        await websocket.send(f.subscribe("/topic/item"))
        testDto = ItemDto(0, 0, 0x61)
        await websocket.send(f.send_json("/app/item", json.dumps(testDto.as_dict())))
        foo = await websocket.recv()
        print(foo)





asyncio.run(test())