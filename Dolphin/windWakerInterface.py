import dolphin_memory_engine as dme
from Dolphin.windWakerResources import *


def hook():
    dme.hook()


def assert_hook():
    dme.assert_hooked()


def write_byte(address, value: int) -> None:
    dme.write_byte(address, value)


def read_byte(address):
    return dme.read_byte(address)


def write_float(address, value) -> None:
    dme.write_float(address, value)


def read_float(address):
    return dme.read_float(address)


def give_item_by_name(item: str):
    if item in player_inventory.keys():
        write_byte(player_inventory[item], item_id_dict[item])


hook()
