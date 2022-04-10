from abc import ABC, abstractmethod
from typing import Dict, List
from Model.itemDto import ItemDto

class AbstractGameHandler(ABC):

    @abstractmethod
    async def connect(self) -> None:
        pass

    @abstractmethod
    async def is_connected(self) -> bool:
        pass

    @abstractmethod
    async def give_item(self, item_id: int) -> bool:
        pass

    @abstractmethod
    async def toggle_event(self, event_type: str, event_index: int, enable: bool) -> None:
        pass

    @abstractmethod
    async def get_items(self) -> Dict[int, int]:
        pass

    @abstractmethod
    async def get_queued_items(self) -> ItemDto:
        pass

    @abstractmethod
    async def clear_queued_items(self) -> None:
        pass
