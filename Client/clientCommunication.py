"""
Handles Requests/Responses to the Back-end.
"""
import asyncio
import json
import websockets
from typing import Callable

from util.clientExceptions import ServerDisconnectWarning
from Client.clientGameConnection import ClientGameConnection

from PySide6.QtCore import Signal, QThread
from util.stompframemanager import StompFrameManager
from Model.multiworldDto import MultiworldDto
from Model.coopDto import CoopDto
from Model.serverConfig import ServerConfig
from Model.multiplayerSetUpDto import MultiplayerSetUpDto
from Model.config import Config
from View.guiWriter import GuiWriter


from base_logger import logging
logger = logging.getLogger(__name__)

class ClientCommunication(GuiWriter):
    world_id: int
    game_room: str
    event_scanning: bool
    player_name: str
    disable_multiplayer: bool
    game_handler: ClientGameConnection
    game_mode_message_handler: Callable

    def __init__(self, config: Config, signal: Signal = None):
        super().__init__(signal)
        self.world_id = config.get_world_id()
        self.game_room = config.get_game_room()
        self.player_name = config.get_player_name()
        self.event_scanning = config.Scanner_Enabled
        self.disable_multiplayer = config.Disable_Multiplayer
        self.game_handler = ClientGameConnection(self.world_id, self.get_signal(), config)
        if config.Game_Mode == "Multiworld":
            self.game_mode_message_handler = multiworld_message_parser
        else:
            self.game_mode_message_handler = coop_message_parser

    async def start_connections(self, server_config: ServerConfig, set_up_dto: MultiplayerSetUpDto) -> None:
        asyncio.create_task(self.game_handler.connect())
        if not self.disable_multiplayer:
            await self.client(server_config)


    async def client(self, server_config: ServerConfig) -> None:
        frame_manager = StompFrameManager(server_config)
        try:
            async with websockets.connect("ws://" + server_config.get_uri()) as client_websocket:
                await self.write(f"Attempting to Connect to {self.game_room}.........")
                await client_websocket.send(frame_manager.connect(server_config.server_ip))
                foo = await client_websocket.recv()
                if not foo.startswith("ERROR"):
                    await client_websocket.send(frame_manager.subscribe(f"/topic/{server_config.game_mode.lower()}/{self.game_room}"))
                    asyncio.create_task(self.listen_to_server(client_websocket))
                    await self.write(f"Successfully connected to the Server")
                    while True:
                        for itemDto in self.game_handler.get_item_to_send():
                            await client_websocket.send(frame_manager.send_json(f"/app/{server_config.game_mode.lower()}/{self.game_room}", json.dumps(itemDto.as_dict())))
                            self.game_handler.remove_item_to_send(itemDto)
                        if QThread.currentThread().isInterruptionRequested():
                            break
                        await asyncio.sleep(.5)
                    # Only gotten to once the loop is broken
                    try:
                        await client_websocket.send(frame_manager.disconnect(""))
                        await client_websocket.close()
                        await self.write("Successfully disconnected from the Server")
                        QThread.currentThread().quit() # Tells thread to fully end
                    except Exception as e:
                        await self.write(f"Error disconnecting from server:\n{e}")

                else:
                    raise ServerDisconnectWarning()
        except ServerDisconnectWarning as sdw:
            await self.write("Failed to Subscribe to the Item Queue. Bad Server URL?")
        except Exception as e:
            await self.write("Problem with Server connection, please check the status with the Server host.")


    async def listen_to_server(self, client_connection) -> None:
        async for message in client_connection:
            a = asyncio.create_task(self.handle_message(message))
            await asyncio.sleep(.15)


    async def handle_message(self, message) -> None:
        if message[:7] == "MESSAGE":
            self.game_mode_message_handler(self, message)

def coop_message_parser(clientFunctions: ClientCommunication, frame: str):
    contents = frame.split("\n")
    coop_dto = CoopDto.from_dict(json.loads(contents[-1][:-1]))
    if coop_dto.sourcePlayerName != clientFunctions.player_name:
        clientFunctions.game_handler.push_item_to_process(coop_dto)

def multiworld_message_parser(clientFunction: ClientCommunication, frame: str):
    contents = frame.split("\n")
    item_dto = MultiworldDto.from_dict(json.loads(contents[-1][:-1]))
    if item_dto.targetPlayerWorldId == clientFunction.world_id and clientFunction.world_id != item_dto.sourcePlayerWorldId:
        clientFunction.game_handler.push_item_to_process(item_dto)