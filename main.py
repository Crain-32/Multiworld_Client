import asyncio
import os
import sys

from Model.serverConfig import ServerConfig
import Client.clientCommunication as clientFunctions
from Model.config import Config

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) # This is your Project Root

print("Using Development version 0.1.2.7")
print("Loading Config...")
config_info = Config.get_config(sys.argv[0][:-7] or ROOT_DIR)
server_config = ServerConfig(config_info.get_address(), config_info.get_port(),
                             config_info.get_world_id(), 'user', 'password')
try:
    asyncio.run(clientFunctions.start_connections(server_config, None, None))
except RuntimeWarning:
    print("Failed to Create Room")
