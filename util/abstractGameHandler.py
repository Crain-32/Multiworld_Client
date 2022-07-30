import asyncio
from abc import ABC, abstractmethod
from typing import Dict, Union, Generator

from Client.types import EventInfo
from Model.ServerDto.coopDto import CoopItemDto
from Model.ServerDto.itemDto import ItemDto


class AbstractGameHandler(ABC):

    @abstractmethod
    async def connect(self) -> None:
        """
        This function should connect the target Game Method with the Client.
        Failure to connect should raise a GameHandlerDisconnectWarning
        """
        pass

    @abstractmethod
    async def is_connected(self) -> bool:
        """
        True if the Game is currently connected. False if not.
        Should not raise an Exception.
        """
        pass

    @abstractmethod
    async def give_item(self, item_id: int) -> bool:
        """
        Giving the Item Successfully should result in a True.
        Failure for any reason should be False.
        Should not raise an Exception.
        """
        pass

    @abstractmethod
    async def toggle_event(self, event_type: str, event_index: int, enable: bool) -> None:
        """
        The bit flag defined by the event_type and event_index should be set to the same value as enable.
        It should raise an EventToggleException if it cannot map the flag input.
        Setting a flag to the same value it currently has is not an Exception.
        """
        pass

    @abstractmethod
    async def watch_events(self) -> Generator[EventInfo, None, None]:
        """
        (Shared/Co-op GameModes only)
        This function should be called after the initial connection Object is made.
        The polling time is left to the implementation, but roughly once per second is recommended.
        Returns a Generator that will yield a new EventInfo Object anytime a new Event flag is changed
        within the game. Which should be sent to the server.
        Should return "None" when the connection is disconnected to terminate the Generator.
        """
        pass

    @abstractmethod
    async def get_items(self) -> Dict[int, int]:
        """
        Return a dictionary of the Item ID : Amount for each Item currently owned.
        Should raise an InvalidItemException if it encounters an unmappable Item Id.
        """
        pass

    @abstractmethod
    async def get_queued_items(self) -> Union[ItemDto, CoopItemDto, None]:
        """
        Returns an ItemDto stored in the Game in the Multiplayer Buffer
        In Coop mode it returns a CoopItemDto
        It can raise an InvalidItemException, however returning None is preferred.
        """
        pass

    @abstractmethod
    async def clear_queued_items(self) -> None:
        """
        This function should clear the current values in the Multiplayer Buffer.
        If it fails to do so, it can raise either a GameHandlerDisconnectWarning, or a CouldNotTakeItemException
        """
        pass

    @abstractmethod
    async def verification_loop(self) -> asyncio.Task:
        """
        Potentially up for deprecation*

        This function should be an endless loop that can verify and update the Current Status of the Game.
        Event Flags, Specific Locations, ect should be included in here. This will primarily help with
        duplication of Chart items if you get the same chart for someone else.
        """
        pass