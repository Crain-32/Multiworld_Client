"""
Handles requests to dolphin.
"""
from typing import Dict
import Dolphin.windWakerInterface as WWI

from Client.abstractGameHandler import AbstractGameHandler


class DolphinGameHandler(AbstractGameHandler):
    def is_connected(self) -> bool:
        return WWI.is_hooked()

    def give_item(self, item_id: int) -> None:
        pass

    def toggle_event(self, event_type: str, event_index: int, enable: bool) -> None:
        pass

    def get_items(self) -> Dict[int, int]:
        pass
