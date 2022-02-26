
import asyncio

from Model.serverConfig import ServerConfig
import Client.clientSocket as clientFunctions
from Model.config import Config

print("Using Client version 0.0.2.1")
print("Loading Config...")
config_info = Config.get_config()
server_config = ServerConfig(config_info.get_address(), config_info.get_port(),
                             config_info.get_world_id(), 'user', 'password')
try:
    asyncio.run(clientFunctions.start_connections(server_config, None, None))
except RuntimeWarning:
    print("Failed to Create Room")