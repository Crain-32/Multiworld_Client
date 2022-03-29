from abc import ABC, abstractmethod
from typing import Dict, List


class AbstractGameHandler(ABC):

    @abstractmethod
    def connect(self) -> None:
        pass

    @abstractmethod
    def is_connected(self) -> bool:
        pass

    @abstractmethod
    def give_item(self, item_id: int) -> bool:
        pass

    @abstractmethod
    def toggle_event(self, event_type: str, event_index: int, enable: bool) -> None:
        pass

    @abstractmethod
    def get_items(self) -> Dict[int, int]:
        pass

    @abstractmethod
    def read_chest_items(self) -> List[int]:
        pass

    @abstractmethod
    def clear_chest_items(self) -> None:
        pass
