"""
Handles Requests/Responses to the Back-end.
"""
import asyncio
import json
import websockets

from util.clientExceptions import ServerDisconnectWarning
from Client.clientGameConnection import ClientGameConnection

from PySide6.QtCore import Signal, QThread
from util.stompframemanager import StompFrameManager
from Model.itemDto import ItemDto
from Model.serverConfig import ServerConfig
from Model.setUpDto import SetUpDto
from Model.config import Config
from View.guiWriter import GuiWriter

from base_logger import logging
logger = logging.getLogger(__name__)


class ClientCommunication(GuiWriter):
    world_id: int
    game_room: str
    event_scanning: bool
    disable_multiplayer: bool
    game_handler: ClientGameConnection

    def __init__(self, signal: Signal = None):
        super().__init__(signal)
        config = Config.get_config()
        self.world_id = config.get_world_id()
        self.game_room = config.get_game_room()
        self.event_scanning = config.Scanner_Enabled
        self.disable_multiplayer = config.Disable_Multiplayer
        self.game_handler = ClientGameConnection(self.world_id, self.get_signal())

    async def start_connections(self, server_config: ServerConfig, set_up_dto: SetUpDto) -> None:
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
                    await client_websocket.send(frame_manager.subscribe(f"/topic/item/{self.game_room}"))
                    asyncio.create_task(self.listen_to_server(client_websocket))
                    await self.write(f"Successfully connected to the Server")
                    while True:
                        for itemDto in self.game_handler.get_item_to_send():
                            await client_websocket.send(frame_manager.send_json(f"/app/item/{self.game_room}", json.dumps(itemDto.as_dict())))
                            self.game_handler.remove_item_to_send(itemDto)
                        if QThread.currentThread().isInterruptionRequested():
                            break
                        await asyncio.sleep(0)
                    # Only gotten to once the loop is broken
                    try:
                        await client_websocket.send(frame_manager.disconnect(""))
                        await client_websocket.close()
                        await self.write("Successfully disconnected from the Server")
                        QThread.currentThread().quit()  # Tells thread to fully end
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
            await asyncio.sleep(0)

    async def handle_message(self, message) -> None:
        if message[:7] == "MESSAGE":
            contents = message.split("\n")
            item_dto = ItemDto.from_dict(json.loads(contents[-1][:-1]))
            if item_dto.targetPlayerWorldId == self.world_id:
                self.game_handler.push_item_to_process(item_dto)
