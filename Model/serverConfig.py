from dataclasses import dataclass, asdict


@dataclass
class ServerConfig:
    server_ip: str
    server_port: int
    worldId: int
    userName: str
    password: str

    def as_dict(self):
        return asdict(self)


