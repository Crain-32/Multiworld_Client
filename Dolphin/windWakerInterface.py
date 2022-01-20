import dolphin_memory_engine as dme

from Dolphin.windWakerResources import *


def hook():
    dme.hook()


def assert_hook():
    dme.assert_hooked()


def is_hooked():
    return dme.is_hooked()


def write_byte(address, value: int) -> None:
    dme.write_byte(address, value)


def read_byte(address):
    return dme.read_byte(address)


def read_word(address):
    return dme.read_word(address)


def write_word(address, value):
    return dme.write_word(address, value)


def write_float(address, value) -> None:
    dme.write_float(address, value)


def read_float(address):
    return dme.read_float(address)


def read_chest_items():
    return [read_word(0x803FF6C8), read_word(0x803FF6C)]


def clear_chest_items():
    return [write_word(0x803FF6C8, 0x00), write_word(0x803FF6C)]


def give_item_by_value(item: int):
    for name, item_val in item_id_dict.items():
        if item_val == item and name in player_inventory:
            print(name + " was found for item ID - " + str(item))
            write_byte(player_inventory[name], item)


def give_item_by_name(item: str):
    give_item_by_value(item_id_dict[item])
