import asyncio
import json
import ssl

import requests
import websockets

from Model.ServerDto.createGameRoomDto import CreateGameRoomDto
from Model.ServerDto.itemDto import ItemDto
from Model.ServerDto.playerDto import PlayerDto
# from Model.config import Config
from base_logger import logging
from util.clientHttpUtil import SslHttpAdapter
from util.stompframemanager import StompFrameManager

logger = logging.getLogger(__name__)

address = "twwmultiplayer.com"
port = 8081
world_id = 1
game_room = "qwert"
room_password = "qwert"
player_name = "Crain1"
target_url = f"//{address}:{port}"
httpSession = requests.Session()
httpSession.mount(f"https://{target_url}", SslHttpAdapter())
context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

def check_empty():
    response = httpSession.get(f"https:{target_url}/rest/gameroom/empty", verify=False)
    if response.status_code == 200:
        print(response.json())
    else:
        print(response.text)


def check_gameroom():
    response = httpSession.get(f"https:{target_url}/rest/gameroom", verify=False)
    if response.status_code == 200:
        print(response.json())
    else:
        print(response.text)

def create_gameroom():
    response = httpSession.get(f"https:{target_url}/rest/gameroom", verify=False)
    # game_room_name = str(len(response.json()))
    game_room_name = "7"
    gameRoom = CreateGameRoomDto(worldAmount=world_id, playerAmount=world_id+1, gameRoomName=game_room_name, gameRoomPassword=room_password)
    global game_room
    game_room = game_room_name
    response = httpSession.post(f"https:{target_url}/rest/gameroom", json=gameRoom.as_dict(), verify=False)
    if response.status_code >= 300:
        print(response.json())
        raise RuntimeError("Failed To Create a GameRoom!")

def create_player(player: PlayerDto):
    response = httpSession.post(f"https:{target_url}/rest/gameroom/{game_room}?password={room_password}", json=player.as_dict(), verify=False)
    print(response)
    if response.status_code >= 300:
        print(response.json())
        raise RuntimeError("Failed To Add Player!")

async def test():
    # create_gameroom()
    player = PlayerDto(player_name, world_id, "SHARED")
    create_player(player)
    async with websockets.connect(f"wss:{target_url}/ws", ssl=context, extra_headers={"sessionId": None}) as websocket:
        print(websocket.path)
        print(websocket.request_headers)
        print(websocket.response_headers)
        print(websocket.subprotocol)
        print(websocket.remote_address)
        print(websocket.local_address)
        f = StompFrameManager(None)
        await websocket.send(f.connect(f"{address}"))
        foo = await websocket.recv()
        print(foo)
        # await websocket.send(f.send_json(f"/app/test", "", room_password))
        # print(f.subscription_num)
        await websocket.send(f.subscribe(f"/topic/multiplayer/{game_room}", room_password))
        # await websocket.send(f.subscribe(f"/topic/general/{game_room}", room_password))
        # await websocket.send(f.subscribe(f"/topic/error/{game_room}", room_password))
        print("Subscribed")
        # foo = await websocket.recv()
        # print(foo)
        test_dto = ItemDto(world_id, 10, 0x34)
        # test_dto = CoopDto("Foobar", 0x34)
        await websocket.send(f.send_json(f"/app/item/{game_room}", json.dumps(test_dto.as_dict()), room_password))
        await websocket.send(f.send_json(f"/app/connect/{game_room}", json.dumps(player.as_dict()), room_password))
        async for message in websocket:
            print(message)

    # check_empty()
    # check_gameroom()
    httpSession.close()

asyncio.run(test())
