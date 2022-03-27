
import asyncio

from Model.serverConfig import ServerConfig
import Client.clientCommunication as clientFunctions
from Model.config import Config

print("Using Development version 0.0.2.4")
print("Loading Config...")
config_info = Config.get_config()
server_config = ServerConfig(config_info.get_address(), config_info.get_port(),
                             config_info.get_world_id(), 'user', 'password')
try:
    asyncio.run(clientFunctions.start_connections(server_config, None, None))
except RuntimeWarning:
    print("Failed to Create Room")
