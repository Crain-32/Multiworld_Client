class CouldNotGiveItemException (Exception):
    """Give item failure"""


class DuplicateItemWarning (UserWarning):
    """Duplicate item"""


class EventToggleException (Exception):
    """Event toggle failure"""


class GameHandlerDisconnectWarning (UserWarning):
    """Game Handler Disconnected"""

# This does say warning,but keep it as Exception (Crain!)
# We always want to catch this, and it's easier to do that as an Exception.
class ServerDisconnectWarning (Exception):
    """Server Disconnected"""

