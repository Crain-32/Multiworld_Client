from configparser import ConfigParser
from os import path


class Config:
    _ConfigInstance = None
    _config_parser = ConfigParser()
    _ServerAddress: str = "http://localhost"
    _Port: int = 8080
    _World_id: int = 0
    _Game_Room: str = ""
    _Max_Players: int = 2
    Game_Mode: str = "Multiworld"
    root_dir: str = "."
    _Player_Name: str = ""
    Scanner_Enabled: bool = False
    Scan_Treasure: bool = False
    Scan_Event_Flags: bool = False
    Scan_Item_Flags: bool = False
    Scan_Dungeon_Rooms: bool = False
    Disable_Multiplayer: bool = False
    Random_Rupoors: bool = False

    @staticmethod
    def get_config(root_dir: str = "."):
        if Config._ConfigInstance is None:
            Config(root_dir)
        return Config._ConfigInstance

    def __init__(self, root_dir: str = "."):
        self.root_dir = root_dir
        self._config_parser.read(path.join(root_dir, "config.ini"))

        if Config._ConfigInstance is not None:
            raise Exception("Cannot have multiple Configs")
        else:
            Config._ConfigInstance = self
            if not path.exists('config.ini'):
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
        with open("config.ini", 'w') as f:
            self._config_parser.write(f)

    def parse_config_file(self):
        self._ServerAddress = self._config_parser.get('SERVER', 'server', fallback="http://twwmultiplayer.com")
        self._Port = int(self._config_parser.get('SERVER', 'port', fallback=8080))
        self.Game_Mode = self._config_parser.get('SERVER', 'gamemode', fallback="Multiworld")

        self._World_id = int(self._config_parser.get('GAME', 'world_id', fallback=1))
        self._Game_Room = self._config_parser.get('GAME', 'gameroom_name', fallback="")
        self._Max_Players = int(self._config_parser.get('GAME', 'max_players', fallback=2))

        self.Scanner_Enabled = bool(self._config_parser.get('GAME', 'scan_flags', fallback=False))
        self.Scan_Treasure = bool(self._config_parser.get('GAME', 'scan_treasure', fallback=False))
        self.Scan_Event_Flags = bool(self._config_parser.get('GAME', 'scan_events', fallback=False))
        self.Scan_Item_Flags = bool(self._config_parser.get('GAME', 'scan_item_pickup', fallback=False))
        self.Scan_Dungeon_Rooms = bool(self._config_parser.get('GAME', 'scan_dungeon_rooms', fallback=False))
        self.Disable_Multiplayer = bool(self._config_parser.get('GAME', 'disable_multiplayer', fallback=False))
        self.Random_Rupoors = bool(self._config_parser.get('GAME', 'random_rupoors', fallback=False))

    def get_address(self):
        return self._ServerAddress

    def get_port(self):
        return self._Port

    def get_world_id(self):
        return self._World_id

    def get_game_room(self):
        return self._Game_Room

    def get_player_name(self):
        return self._Player_Name
