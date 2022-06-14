from dataclasses import dataclass, asdict


@dataclass
class ServerConfig:
    server_ip: str
    server_port: int
    world_id: int
    game_mode: str
    game_room: str
    user_name: str
    password: str

    def as_dict(self):
        return asdict(self)

    def get_uri(self):
        return self.server_ip + ":" + str(self.server_port)

