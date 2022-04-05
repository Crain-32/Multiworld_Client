import asyncio
import os
import sys

from Model.serverConfig import ServerConfig
from Client.clientCommunication import ClientCommunication
from Model.config import Config

from base_logger import logging
logger = logging.getLogger(__name__)

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) # This is your Project Root

logger.info("Using Development version 0.1.2.7")
logger.info("Loading Config...")

config_info = Config.get_config(sys.argv[0][:-7] or ROOT_DIR)

server_config = ServerConfig(config_info.get_address(), config_info.get_port(),
                             config_info.get_world_id(), 'user', 'password')
clientFunctions = ClientCommunication(config_info)
try:
    asyncio.run(clientFunctions.start_connections(server_config, None))
except RuntimeWarning:
    logger.error("Failed to Create Room")
