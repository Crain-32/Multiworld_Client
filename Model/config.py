from configparser import ConfigParser
from os import path

from main_paths import CONFIG_PATH


class Config:
    _ConfigInstance = None
    _config_parser = ConfigParser()
    Server_Address: str
    Port: int
    World_id: int
    Game_Room: str
    Max_Worlds: int
    Game_Mode: str
    root_dir: str
    Player_Name: str
    Password: str
    Scanner_Enabled: bool
    Scan_Treasure: bool
    Scan_Event_Flags: bool
    Scan_Item_Flags: bool
    Scan_Dungeon_Rooms: bool
    Disable_Multiplayer: bool
    Random_Rupoors: bool

    World_Id_Location: int
    Item_Id_Location: int

    @staticmethod
    def get_config():
        if Config._ConfigInstance is None:
            Config()
        return Config._ConfigInstance

    def __init__(self):
        self._config_parser.read(CONFIG_PATH)

        if Config._ConfigInstance is not None:
            raise Exception("Cannot have multiple Configs")
        else:
            Config._ConfigInstance = self
            if not path.exists(CONFIG_PATH):
                self.write_default()

            self.parse_config_file()

    def write_default(self):
        self._config_parser.add_section('SERVER')
        self._config_parser['SERVER']['server'] = "twwmultiplayer.com"
        self._config_parser['SERVER']['port'] = "8080"
        self._config_parser['SERVER']['gamemode'] = "Multiworld"

        self._config_parser.add_section('GAME')
        self._config_parser['GAME']['world_id'] = "1"
        self._config_parser['GAME']['gameroom_name'] = ""
        self._config_parser['GAME']['random_rupoors'] = ""
        self._config_parser['GAME']['max_players'] = "2"

        self._config_parser.add_section('DOLPHIN')
        self._config_parser['DOLPHIN']['world_id_location'] = "0x803FED90"
        self._config_parser['DOLPHIN']['item_id_location'] = "0x803FED94"
        with open(CONFIG_PATH, 'w') as f:
            self._config_parser.write(f)

    def parse_config_file(self):
        self.Server_Address = self._config_parser.get('SERVER', 'server', fallback="twwmultiplayer.com")
        self.Port = int(self._config_parser.get('SERVER', 'port', fallback=8080))
        self.Game_Mode = self._config_parser.get('SERVER', 'gamemode', fallback="Multiworld")
        self.Password = self._config_parser.get('SERVER', 'password', fallback="")

        self.World_id = int(self._config_parser.get('GAME', 'world_id', fallback=1))
        self.Game_Room = self._config_parser.get('GAME', 'gameroom_name')
        self.Max_Worlds = int(self._config_parser.get('GAME', 'max_worlds', fallback=2))
        self.Player_Name = self._config_parser.get('GAME', 'player_name', fallback="")

        self.Scanner_Enabled = bool(self._config_parser.get('GAME', 'scan_flags', fallback=False))
        self.Scan_Treasure = bool(self._config_parser.get('GAME', 'scan_treasure', fallback=False))
        self.Scan_Event_Flags = bool(self._config_parser.get('GAME', 'scan_events', fallback=False))
        self.Scan_Item_Flags = bool(self._config_parser.get('GAME', 'scan_item_pickup', fallback=False))
        self.Scan_Dungeon_Rooms = bool(self._config_parser.get('GAME', 'scan_dungeon_rooms', fallback=False))
        self.Disable_Multiplayer = bool(self._config_parser.get('GAME', 'disable_multiplayer', fallback=False))
        self.Random_Rupoors = bool(self._config_parser.get('GAME', 'random_rupoors', fallback=False))

        self.World_Id_Location = int(self._config_parser.get('DOLPHIN', 'world_id_location', fallback=0x803FED90), 16)
        self.Item_Id_Location = int(self._config_parser.get('DOLPHIN', 'item_id_location', fallback=0x803FED94), 16)

    def get_uri(self):
        return self.Server_Address + ":" + str(self.Port)
