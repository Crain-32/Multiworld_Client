import uuid
from typing import Optional, Dict, AnyStr

from Model.serverConfig import ServerConfig


def parse_headers(headers: Dict[str, str]) -> str:
    result = ""
    for key, val in headers.items():
        result += "{}:{}\x0A".format(key, val)
    return result


def base_frame_template(command: str) -> str:
    return command + "\x0A{}\x0A{}\x00"


class StompFrameManager:

    def __init__(self, serverConfig: ServerConfig) -> None:
        self.serverConfig = serverConfig
        self.subscription_num = uuid.uuid4()
        self.subscriptions = dict()

    def get_target_header(self, message: AnyStr, target_header: AnyStr) -> str:
        segments = message.split("\n")
        for segment in segments[1:]:
            header, value = segment.split(":")
            if header == target_header:
                return value
        return None

    def connect(self, host) -> str:
        frame = base_frame_template("CONNECT")
        header = {"accept-version": "1.2",
                  "host": host}

        header_str = parse_headers(header)
        return frame.format(header_str, "")

    def subscribe(self, destination:str, password=None) -> Optional[str]:
        if destination in self.subscriptions.keys():
            return None
        frame = base_frame_template("SUBSCRIBE")
        header = {"id": str(self.subscription_num),
                  "destination": destination,
                  "password": password if password is not None else self.serverConfig.password,
                  "ack": "auto"}
        self.subscriptions[destination] = self.subscription_num
        self.subscription_num = uuid.uuid4()
        header_str = parse_headers(header)
        return frame.format(header_str, "")

    def send(self, destination, payload, payload_type, password=None) -> str:
        frame = base_frame_template("SEND")
        header = {"destination": destination,
                  "content-type": payload_type,
                  "content-length": str(len(payload)),
                  "password": password if password is not None else self.serverConfig.password}
        header_str = parse_headers(header)
        return frame.format(header_str, payload)

    def send_text(self, destination, payload) -> str:
        return self.send(destination, payload, "text/plain", "")

    def send_json(self, destination, payload, password=None) -> str:
        return self.send(destination, payload, "application/json", password)

    def ack(self, headers) -> str:
        frame = base_frame_template("ACK")
        return frame.format(headers, "")

    def nack(self, headers) -> str:
        frame = base_frame_template("NACK")
        return frame.format(headers, "")

    def begin(self, transaction_id) -> str:
        frame = base_frame_template("BEGIN")
        header = {"transaction": transaction_id}
        header_str = parse_headers(header)
        return frame.format(header_str, "")

    def commit(self, transaction_id) -> str:
        frame = base_frame_template("COMMIT")
        header = {"transaction": transaction_id}
        header_str = parse_headers(header)
        return frame.format(header_str, "")

    def abort(self, transaction_id) -> str:
        frame = base_frame_template("ABORT")
        header = {"transaction": transaction_id}
        header_str = parse_headers(header)
        return frame.format(header_str, "")

    def disconnect(self, receipt_id) -> str:
        frame = base_frame_template("DISCONNECT")
        header = {"receipt": receipt_id}
        header_str = parse_headers(header)
        return frame.format(header_str, "")
