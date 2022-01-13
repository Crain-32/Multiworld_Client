import Dolphin.windWakerInterface as windWakerGame
import Dolphin.windWakerResources as windWakerResources

from PySide6.QtWidgets import *

from View.uiItemTestingMenu import uiItemTestingMenu


class ItemTestingWindow(QMainWindow):

    def __init__(self):
        super(ItemTestingWindow, self).__init__()
        self.ui = uiItemTestingMenu()
        self.ui.setupUi(self)
        self.ui.itemSelection.addItems(windWakerResources.item_id_dict.keys())
        self.ui.itemSelection.itemClicked.connect(self.item_selected_event)
        self.ui.sendToMe.clicked.connect(self.give_item_to_player)
        self.show()
        self.selectedItemName = ""

    def item_selected_event(self, item):
        self.selectedItemName = item.text()

    def give_item_to_player(self):
        windWakerGame.give_item_by_name(self.selectedItemName)
