import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from View.multiworldClient import MultiworldClientWindow
from View.itemTestingMenu import ItemTestingWindow

app = QApplication(sys.argv)

if len(sys.argv) > 1:
    window = ItemTestingWindow()
else:
    window = MultiworldClientWindow()

sys.exit(app.exec())
