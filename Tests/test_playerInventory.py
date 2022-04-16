import json
from unittest.mock import MagicMock, call

import pytest

from Client.types import ItemInfo
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

    class TestCreateInventory:
        def test_create_inventory(self):
            base_inventory: ItemInfo = ItemInfo([{
                "Progressive Bow": {
                    "item_ids": [39, 53, 54],
                    "max_amount": 3
                }
            }, {
                "Earth God's Lyric": {
                    "item_id": 112,
                    "max_amount": 1
                }
            }])

            player_inventory = PlayerInventory()

            player_inventory.create_inventory(base_inventory)

            assert player_inventory.item_name_inventory_item_dict == \
                   {
                       'Progressive Bow': InventoryItem(item_name='Progressive Bow', curr_amount=0, max_amount=3),
                       "Earth God's Lyric": InventoryItem(item_name="Earth God's Lyric", curr_amount=0, max_amount=1),
                       'Junk': InventoryItem(item_name='Junk', curr_amount=0, max_amount=-1)
                   }

            with open('./item_id_item_name_dict_junk.json') as file:
                d = json.load(file)
                item_id_item_name_dict_assert = {int(k): v for k, v in d.items()}

            item_id_item_name_dict_assert[39] = "Progressive Bow"
            item_id_item_name_dict_assert[53] = "Progressive Bow"
            item_id_item_name_dict_assert[54] = "Progressive Bow"
            item_id_item_name_dict_assert[112] = "Earth God\'s Lyric"
            assert player_inventory.item_id_item_name_dict == item_id_item_name_dict_assert

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
