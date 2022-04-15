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

    class TestItemMaxed:
        def test_item_maxed_false(self):
            player_inventory = PlayerInventory()
            player_inventory.item_id_item_name_dict[50] = "item"
            player_inventory.item_name_inventory_item_dict["item"] = InventoryItem(item_name="item", curr_amount=0
                                                                                   , max_amount=99)

            assert player_inventory.item_maxed(50) == False

        def test_item_maxed_false(self):
            player_inventory = PlayerInventory()
            player_inventory.item_id_item_name_dict[50] = "item"
            player_inventory.item_name_inventory_item_dict["item"] = InventoryItem(item_name="item", curr_amount=99
                                                                                   , max_amount=99)

            assert player_inventory.item_maxed(50) == True
