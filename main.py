import os
import sys

from PySide6.QtWidgets import QApplication

from Model.config import Config
from View.multiworldClient import MultiworldClientWindow
from base_logger import logging

logger = logging.getLogger(__name__)

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) # This is your Project Root

logger.debug("Using Development version 0.3.0")
logger.debug("Loading Config...")
config_info = Config.get_config()
app = QApplication(sys.argv)

window = MultiworldClientWindow()

sys.exit(app.exec())
