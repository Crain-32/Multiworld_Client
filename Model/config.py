import sys

class Config:
    _ConfigInstance = None
    _ServerAddress = "localhost"
    _Port = 8080
    _World_id = 0
    _Game_Room = ""

    @staticmethod
    def get_config():
        if Config._ConfigInstance is None:
            Config()
        return Config._ConfigInstance

    def __init__(self):
        if Config._ConfigInstance is not None:
            raise Exception("Cannot have multiple Configs")
        else:
            Config._ConfigInstance = self
            self.read_config_file()

    def read_config_file(self):
        with open(sys.argv[0][:-7] + "/config.txt") as config_file:
            for line in config_file:
                contents = line[:-1].split(":")
                if contents[0] == "server":
                    self._ServerAddress = contents[1].strip()
                    continue
                if contents[0] == "world_id":
                    self._World_id = int(contents[1])
                    continue
                if contents[0] == "port":
                    self._Port = int(contents[1])
                    continue
                if contents[0] == "gameroom_name":
                    self._Game_Room = contents[1]
                    continue

    def get_address(self):
        return self._ServerAddress

    def get_port(self):
        return self._Port

    def get_world_id(self):
        return self._World_id

    def get_game_room(self):
        return self._Game_Room
