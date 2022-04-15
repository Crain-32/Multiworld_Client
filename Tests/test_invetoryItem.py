import pytest

from Model.inventoryItem import InventoryItem
from util.clientExceptions import DuplicateItemWarning


class TestInventoryItem:
    class TestAddItem:
        def test_add(self):
            inventory_item = InventoryItem(item_name="test", curr_amount=0, max_amount=5)
            inventory_item.add_item()

            assert inventory_item.curr_amount == 1

        def test_max_raise_exception(self):
            inventory_item = InventoryItem(item_name="test", curr_amount=5, max_amount=5)

            with pytest.raises(DuplicateItemWarning):
                inventory_item.add_item()

    class TestRemove:
        def test_remove(self):
            inventory_item = InventoryItem(item_name="test", curr_amount=1, max_amount=5)
            inventory_item.remove_item()

            assert inventory_item.curr_amount == 0

        def test_min(self):
            inventory_item = InventoryItem(item_name="test", curr_amount=0, max_amount=5)
            inventory_item.remove_item()

            assert inventory_item.curr_amount == 0

    class TestMax:
        def test_is_max(self):
            inventory_item = InventoryItem(item_name="test", curr_amount=5, max_amount=5)

            assert inventory_item.at_max()

        def test_is_not_max(self):
            inventory_item = InventoryItem(item_name="test", curr_amount=2, max_amount=5)

            assert not inventory_item.at_max()
