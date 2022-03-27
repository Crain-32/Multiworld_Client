from abc import ABC, abstractmethod
from typing import Dict, Coroutine


class AbstractGameHandler(ABC):

    @abstractmethod
    def is_connected(self) -> bool:
        pass

    @abstractmethod
    def give_item(self, item_id: int) -> None:
        pass

    @abstractmethod
    def toggle_event(self, event_type: str, event_index: int, enable: bool) -> None:
        pass

    @abstractmethod
    def get_items(self) -> Dict[int, int]:
        pass

