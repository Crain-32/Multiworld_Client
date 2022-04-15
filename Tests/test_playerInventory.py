from unittest.mock import MagicMock, call

import pytest

from Model.inventoryItem import InventoryItem
from util.clientExceptions import InvalidItemException
from util.playerInventory import PlayerInventory


class TestPlayerInventory:
    class TestItemIdCheck:
        def test_is_in_dict(self):
            player_inventory = PlayerInventory()
            player_inventory.item_id_item_name_dict[50] = "item"

            player_inventory.item_id_check(50)

        def test_not_in_dict_raise_InvalidItemException(self):
            player_inventory = PlayerInventory()

            with pytest.raises(InvalidItemException):
                player_inventory.item_id_check(50)

    def test_item_maxed(self):
        player_inventory = PlayerInventory()
        player_inventory.item_id_item_name_dict[50] = "item"

        inventory_item = InventoryItem(item_name="item", curr_amount=1, max_amount=99)
        inventory_item.at_max = MagicMock()
        player_inventory.item_name_inventory_item_dict["item"] = inventory_item

        player_inventory.item_maxed(50)

        inventory_item.at_max.assert_called_once()

    def test_give_item(self, mocker):
        player_inventory = PlayerInventory()

        player_inventory.item_id_item_name_dict[50] = "item"

        inventory_item = InventoryItem(item_name="item", curr_amount=1, max_amount=99)
        inventory_item.add_item = MagicMock()
        player_inventory.item_name_inventory_item_dict["item"] = inventory_item

        player_inventory.give_item(50)

        inventory_item.add_item.assert_called_once()

    def test_set_starting_items(self):
        player_inventory = PlayerInventory()
        player_inventory.give_item = MagicMock()

        player_inventory.set_starting_items([15, 16, 17])

        player_inventory.give_item.assert_has_calls(calls=[call(15), call(16), call(17)])
