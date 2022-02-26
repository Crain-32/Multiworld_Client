import sys

class Config:
    _ConfigInstance = None
    _ServerAddress = "localhost"
    _Port = 8080
    _World_id = 0
    _Game_Room = ""
    Scanner_Enabled = False
    Scan_Treasure = False
    Scan_Event_Flags = False
    Scan_Item_Flags = False
    Scan_Dungeon_Rooms = False
    Disable_Multiplayer = False
    Random_Rupoors = False

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
                elif contents[0] == "world_id":
                    self._World_id = int(contents[1])
                elif contents[0] == "port":
                    self._Port = int(contents[1])
                elif contents[0] == "gameroom_name":
                    self._Game_Room = contents[1]
                elif contents[0] == "scan_flags":
                    self.Scanner_Enabled = bool(contents[1])
                elif contents[0] == "scan_treasure":
                    self.Scan_Treasure = bool(contents[1])
                elif contents[0] == "scan_events":
                    self.Scan_Event_Flags = bool(contents[1])
                elif contents[0] == "scan_item_pickup":
                    self.Scan_Item_Flags = bool(contents[1])
                elif contents[0] == "scan_dungeon_rooms":
                    self.Scan_Dungeon_Rooms = bool(contents[1])
                elif contents[0] == "disable_multiplayer":
                    self.Disable_Multiplayer = bool(contents[1])
                elif contents[0] == "random_rupoors":
                     self.Random_Rupoors = bool(contents[1])

    def get_address(self):
        return self._ServerAddress

    def get_port(self):
        return self._Port

    def get_world_id(self):
        return self._World_id

    def get_game_room(self):
        return self._Game_Room

