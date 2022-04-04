from PySide6.QtCore import Signal

from base_logger import logging
logger = logging.getLogger(__name__)

class GuiLogger:
    gui_log_signal: Signal

    def __init__(self, signal: Signal = None): # Signal defaults to None so that running from terminal still works
        self.gui_log_signal = signal

    async def log(self, message: str, terminal_only: bool = False) -> None:
        if self.gui_log_signal is None or terminal_only:
            logger.info(message)
        else:
            self.gui_log_signal.emit(str(message))

    def get_signal(self) -> Signal:
        return self.gui_log_signal