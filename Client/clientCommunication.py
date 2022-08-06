"""
Handles Requests/Responses to the Back-end.
"""
import asyncio
import json
import ssl
from typing import Dict, AnyStr, Callable

import websockets
from PySide6.QtCore import Signal, QThread

from Client.clientGameConnection import ClientGameConnection
from Model.ServerDto.coopDto import CoopItemDto
from Model.ServerDto.itemDto import ItemDto
from Model.ServerDto.playerDto import PlayerDto
from Model.config import Config
from Model.serverConfig import ServerConfig
from View.guiWriter import GuiWriter
from base_logger import logging
from util.clientExceptions import ServerDisconnectWarning
from util.stompframemanager import StompFrameManager

logger = logging.getLogger(__name__)


class ClientCommunication(GuiWriter):
    world_id: int
    game_room: str
    event_scanning: bool
    player_name: str
    disable_multiplayer: bool
    game_mode: str
    frame_manager: StompFrameManager
    game_handler: ClientGameConnection
    player_names: Dict[int, AnyStr]
    item_dto_parser: Callable[[AnyStr], None]

    def __init__(self, config: Config, signal: Signal = None):
        super().__init__(signal)
        self.world_id = config.World_id
        self.game_room = config.Game_Room
        self.player_name = config.Player_Name
        self.event_scanning = config.Scanner_Enabled
        self.disable_multiplayer = config.Disable_Multiplayer
        self.game_mode = config.Game_Mode
        self.game_handler = ClientGameConnection(self.world_id, self.get_signal(), config)
        self.item_dto_parser = self.multiplayer_item_dto_parser
        if config.Game_Mode.upper() == "COOP":
            self.log("COOP Mode Enabled")
            self.item_dto_parser = self.coop_item_dto_parser

    async def start_connections(self, server_config: ServerConfig) -> None:
        asyncio.create_task(self.game_handler.connect())
        await self.client(server_config)

    async def client(self, server_config: ServerConfig) -> None:
        self.frame_manager = StompFrameManager(server_config)
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        logger.debug("CONNECTING TO SERVER")
        # if "localhost" in server_config.get_uri(): Disabled till the TLS cert is ready
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        try:
            async with websockets.connect("ws://" + server_config.get_uri() + "/ws",
                                          extra_headers={"sessionId": None}) as client_websocket:
                await self.write(f"Attempting to Connect to {self.game_room}.........")
                await client_websocket.send(self.frame_manager.connect(server_config.server_ip))
                connected_frame = await client_websocket.recv()
                if not connected_frame.startswith("ERROR"):
                    await self.write(f"Successfully connected to {self.game_room}")
                    asyncio.create_task(self.listen_to_server(client_websocket))
                    if self.game_mode.upper() != "COOP":
                        await client_websocket.send(
                            self.frame_manager.subscribe(f"/topic/multiplayer/{self.game_room}"))
                        await self.write(f"Subscribed to {self.game_room}'s Multiworld Queue")
                    else:
                        await client_websocket.send(self.frame_manager.subscribe(f"/topic/coop/{self.game_room}"))
                        await self.write(f"Subscribed to {self.game_room}'s Coop Queue")
                    await self.write(f"Subscribed to {self.game_room}'s Item Queue")
                    await client_websocket.send(self.frame_manager.subscribe(f"/topic/event/{self.game_room}"))
                    await self.write(f"Subscribed to {self.game_room}'s Event Queue")

                    await client_websocket.send(self.frame_manager.send_json(f"/app/connect/{self.game_room}",
                                                                             json.dumps(PlayerDto(
                                                                                 playerName=self.player_name).as_dict())))
                    await client_websocket.send(self.frame_manager.subscribe(f"/topic/names/{self.game_room}"))
                    await self.write(f"Subscribed to {self.game_room}'s Name Queue")
                    await client_websocket.send(self.frame_manager.subscribe(f"/topic/error/{self.game_room}"))
                    await self.write(f"Subscribed to {self.game_room}'s Error Queue")
                    await client_websocket.send(self.frame_manager.subscribe(f"/topic/general/{self.game_room}"))
                    await self.write(f"Subscribed to {self.game_room}'s General Queue")


                    while not QThread.currentThread().isInterruptionRequested():
                        for itemDto in self.game_handler.get_item_to_send():
                            await client_websocket.send(self.frame_manager.send_json(f"/app/{server_config.game_mode.lower()}/{self.game_room}", json.dumps(itemDto.as_dict())))
                            self.game_handler.remove_item_to_send(itemDto)
                        await asyncio.sleep(.5)
                    # Only gotten to once the loop is broken
                    try:
                        await client_websocket.send(self.frame_manager.disconnect(""))
                        await client_websocket.close()
                        await self.write("Successfully disconnected from the Server")
                        QThread.currentThread().quit()  # Tells thread to fully end
                    except Exception as e:
                        await self.write(f"Error disconnecting from server:\n{e}")

                else:
                    raise ServerDisconnectWarning()
        except ServerDisconnectWarning as sdw:
            await self.write("Failed to Subscribe to the Item Queue. Bad Server URL?")
            self.log("\n".join(sdw.args))
        except Exception as e:
            await self.write("Problem with Server connection, please check the status with the Server host.")
            self.log("\n".join(e.args))

    async def listen_to_server(self, client_connection) -> None:
        async for message in client_connection:
            a = asyncio.create_task(self.handle_message(message))
            await asyncio.sleep(.15)

    async def handle_message(self, message) -> None:
        if message[:5] == "ERROR":
            self.log(message)
        if message[:7] != "MESSAGE":
            return None
        try:
            target_destination = self.frame_manager.get_target_header(message, "destination").split("/")[2]
            if target_destination == "multiplayer":
                self.item_dto_parser(message)
            elif target_destination == "event":
                pass  # We do nothing for events yet
            elif target_destination == "error":
                await self.write(f"The Server sent an Error, check the Logs for more information", False)
                self.log(message)
            elif target_destination == "names":
                pass  # We do nothing for Names yet
            elif target_destination == "general":
                await self.write(
                    f"The Server will be shutting {self.game_room} down due to a lack of Connected Players")
            elif target_destination == "coop":
                self.item_dto_parser(message)
            else:
                await self.write(f"The Server sent an unknown message, check the Logs for more information", False)
                self.log(f"Unknown Destination Header Sent: {target_destination}\n{message}")
        finally:
            pass

    def multiplayer_item_dto_parser(self, frame: str):
        contents = frame.split("\n")
        item_dto: ItemDto = ItemDto.from_dict(json.loads(contents[-1][:-1]))
        if item_dto.targetPlayerWorldId == self.world_id and self.world_id != item_dto.sourcePlayerWorldId:
            self.game_handler.push_item_to_process(item_dto)

    def coop_item_dto_parser(self, frame: str):
        contents = frame.split("\n")
        item_dto: CoopItemDto = CoopItemDto.from_dict(json.loads(contents[-1][:-1]))
        if self.player_name != item_dto.sourcePlayer:
            self.game_handler.push_item_to_process(item_dto)
