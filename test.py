import asyncio
import json

import websockets

from base_logger import logging
logger = logging.getLogger(__name__)

from Client.stompframemanager import StompFrameManager
from Model.itemDto import ItemDto
#from Model.config import Config

address = "twwmultiplayer.com"
port = 8080
world_id = 2
game_room = "testing"


async def test():
    async with websockets.connect(f"ws://{address}:{port}/ws") as websocket:
        f = StompFrameManager(None)
        await websocket.send(f.connect(f"{address}"))
        foo = await websocket.recv()
        logger.info(foo)
        logger.info(websocket.id)
        await websocket.send(f.subscribe(f"/topic/item/{game_room}"))
        logger.info("Subscribed")
        test_dto = ItemDto(world_id, 0, 0x23)
        await websocket.send(f.send_json(f"/app/item/{game_room}", json.dumps(test_dto.as_dict())))
        foo = await websocket.recv()
        logger.info(foo)

asyncio.run(test())
