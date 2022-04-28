import os

from Model.config import Config

from base_logger import logging
import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from View.multiworldClient import MultiworldClientWindow
from View.itemTestingMenu import ItemTestingWindow

logger = logging.getLogger(__name__)

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) # This is your Project Root

logger.debug("Using Development version 0.3.0")
logger.debug("Loading Config...")
config_info = Config.get_config()
app = QApplication(sys.argv)

if len(sys.argv) > 1:
    window = ItemTestingWindow()
else:
    window = MultiworldClientWindow()

sys.exit(app.exec())
