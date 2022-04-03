from types import MethodType
from typing import List, Dict

import pytest
from Client.clientGameConnection import ClientGameConnection
from util.abstractGameHandler import AbstractGameHandler
from Model.itemDto import ItemDto


class MockedAbstractGameHandler(AbstractGameHandler):

    async def is_connected(self) -> bool:
        pass

    async def give_item(self, item_id: int) -> bool:
        return True

    async def toggle_event(self, event_type: str, event_index: int, enable: bool) -> None:
        pass

    async def get_items(self) -> Dict[int, int]:
        pass

    async def get_queued_items(self) -> List[int]:
        pass

    async def clear_queued_items(self) -> None:
        pass

    async def connect(self) -> None:
        pass


def mock_init(self: ClientGameConnection, world_id: int):
    self._console_handler = MockedAbstractGameHandler()
    self.log = MethodType(nonce_async, ClientGameConnection)


async def nonce_async(*args, **kwargs):
    print('nonce_async')
    return


def nonce(*args, **kwargs):
    return


class TestClientGameConnection:
    _world_id = 1

    @pytest.mark.asyncio
    async def test_process_items(self, monkeypatch):
        monkeypatch.setattr(ClientGameConnection, name='__init__', value=mock_init)
        monkeypatch.setattr(ItemDto, name='get_simple_output', value=nonce)

        client_game_connection = ClientGameConnection(self._world_id)
        client_game_connection._items_to_process = [ItemDto(0, 0, 0)]

        await client_game_connection.process_items()

        assert len(client_game_connection._items_to_process) == 0
