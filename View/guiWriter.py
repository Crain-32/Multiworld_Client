from PySide6.QtCore import Signal

import time

from base_logger import logging
logger = logging.getLogger(__name__)

class GuiWriter:
    gui_log_signal: Signal

    def __init__(self, signal: Signal = None): # Signal defaults to None so that running from terminal still works
        self.gui_log_signal = signal

    def write_message(self, message: str) -> None:
        if self.gui_log_signal is None:
            print(message)
        else:
            self.gui_log_signal.emit(message)

    async def write(self, message: str, put_in_logs: bool = True, log_level: int = logging.WARNING) -> None:
        self.write_message(message)
        if put_in_logs:
            self.log(message, log_level)
    
    def log(self, message: str, log_level: int = logging.WARNING) -> None:
        logger.log(log_level, message)

    def get_signal(self) -> Signal:
        return self.gui_log_signal
