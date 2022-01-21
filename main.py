
import asyncio

from Model.serverConfig import ServerConfig
from Model.setUpDto import SetUpDto
import Client.clientSocket as clientFunctions

print("Loading Config...")
config_info = []
with open("./config.txt") as file:
    for line in file:
        config_info.append(line[:-1].split(":")[1])
server_config = ServerConfig(config_info[0], int(config_info[1]),
                             int(config_info[2]), 'user', 'password') # User/Password not implemented in Server *yet*
set_up_dto = SetUpDto(int(config_info[3]), config_info[4], None, False) # This will change with the above.
try:
    print("Starting Client...")
    asyncio.run(clientFunctions.client(server_config, set_up_dto, None))
except RuntimeWarning:
    print("Failed to Create Room")