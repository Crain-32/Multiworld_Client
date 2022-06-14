import ssl
from typing import AnyStr

import requests
from requests.adapters import HTTPAdapter
from urllib3.poolmanager import PoolManager

from Client.ServerInfo import *
from Model.ServerDto.createGameRoomDto import CreateGameRoomDto
from Model.ServerDto.playerDto import PlayerDto
from Model.config import Config
from base_logger import logging
from util.clientExceptions import InvalidGameRoomException, InvalidPlayerException

logger = logging.getLogger(__name__)

class SslHttpAdapter(HTTPAdapter):

    def init_poolmanager(self, connections, maxsize, block=False, **pool_kwargs):
        self.poolmanager = PoolManager(
            num_pools=connections, maxsize=maxsize, block=block, ssl_version=ssl.PROTOCOL_TLS_CLIENT
        )


def create_game_room(config: Config, password: AnyStr):
    with requests.Session() as httpSession:
        httpSession.mount(f"https://{config.get_uri()}", SslHttpAdapter())
        dto = CreateGameRoomDto.from_client_config(config, password)
        response = httpSession.post(f"https://{config.get_uri()}{create_game_room_endpoint}", json=dto.as_dict(), verify=False)
        if response.status_code >= 300:
            logging.debug(f"Server returned a {response.status_code}")
            logging.debug(response.json())
            raise InvalidGameRoomException("The Game Room could not be created")


def create_player(config: Config, password: AnyStr):
    with requests.Session() as httpSession:
        httpSession.mount(f"https://{config.get_uri()}", SslHttpAdapter())
        dto = PlayerDto.from_config(config)
        check_response = check_player_status(config, httpSession, dto, password)
        if check_response.playerName == dto.playerName:
            return check_response.connected is not True
        response = httpSession.post(f"https://{config.get_uri()}{add_player_endpoint.format(GameRoom=config.Game_Room)}?password={password}", json=dto.as_dict(), verify=False)
        if response.status_code >= 300:
            logging.debug(f"Server returned a {response.status_code}")
            logging.debug(response.json())
            raise InvalidPlayerException(f"Your player could not be added to {config.Game_Mode}")
        return True

def check_player_status(config: Config, httpSession: requests.Session, dto: PlayerDto, password: AnyStr):
    response = httpSession.post(f"https://{config.get_uri()}{check_player_endpoint.format(GameRoom=config.Game_Room)}?password={password}", json=dto.as_dict(), verify=False)
    if response.status_code == 404:
        raise InvalidGameRoomException(f"The provided Game Room/Password Combo does not exist.")
    return PlayerDto.from_dict(response.json())