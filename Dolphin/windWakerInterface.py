import dolphin_memory_engine as dme

import Dolphin.windWakerResources as WWR


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
    return [read_word(0x803FF6FD), read_word(0x803FF701)]


def clear_chest_items():
    return [write_word(0x803FF6FD, 0x0000), write_word(0x803FF701, 0x0000)]


def give_item_by_value(item: int):
    if item in WWR.inventory_handling:
        give_inventory_item_by_value(item)
    elif item in WWR.rupees:
        give_rupees(rupee_map[item])
    elif item in WWR.swords:
        upgrade_sword()
    elif item in WWR.shields:
        upgrade_shield()
    elif item in WWR.shards:
        give_triforce_shard(item & 0xF)
    elif item == 0x50:
        give_bottle()
    elif item == 0x28:
        give_power_bracelets()
    else:
        pass


def give_inventory_item_by_value(item: int):
    write_byte(WWR.player_inventory[WWR.item_name_dict[item]], item)


def remove_inventory_item_by_value(item: int):
    write_byte(WWR.player_inventory[WWR.item_name_dict[item]], 0xFF)


def give_item_by_name(item: str):
    give_inventory_item_by_value(WWR.item_id_dict[item])


def give_power_bracelets():
    dme.write_byte(0x803C4C18, 0x28)
    dme.write_byte(0x803C4CBD, 0x01)


def remove_power_bracelets():
    dme.write_byte(0x803C4C18, 0xFF)
    dme.write_byte(0x803C4CBE, 0x01)


def give_map_by_id(item_id: int):
    pass


def give_rupees(amount: int):
    dme.write_byte(0x803CA768, amount)


def upgrade_sword():
    curr_val = dme.read_byte(0x803C4C16)
    if curr_val == 0x00:
        curr_val = 0x37  # Undershoot by one so no logic changes
    if curr_val == 0x3A:
        curr_val = 0x3D
    dme.write_byte(0x803C4C16, (curr_val + 1))
    curr_val = dme.read_byte(0x803C4CBC)
    dme.write_byte(0x803C4CBC, ((curr_val << 1) + 1))


def downgrade_sword():
    curr_val = dme.read_byte(0x803C4C16)
    if curr_val == 0x38:
        curr_val = 0x01
    if curr_val == 0x3E:
        curr_val = 0x3B
    dme.write_byte(0x803C4C16, (curr_val - 1))
    curr_val = dme.read_byte(0x803C4CBC)
    dme.write_byte(0x803C4CBC, (curr_val >> 1))


def upgrade_shield():
    curr_val = dme.read_byte(0x803C4C17)
    if curr_val == 0x00:
        curr_val = 0x3A
    dme.write_byte(0x803C4C17, (curr_val + 1))
    curr_val = dme.read_byte(0x803C4C17)
    dme.write_byte(0x803C4CBD, (curr_val << 1) + 1)


def downgrade_shield():
    curr_val = dme.read_byte(0x803C4C17)
    if curr_val == 0x3B:
        curr_val = 0x01
    dme.write_byte(0x803C4C17, (curr_val - 1))
    curr_val = dme.read_byte(0x803C4C17)
    dme.write_byte(0x803C4CBD, (curr_val >> 1))


def give_triforce_shard(shard_num: int):
    curr_shards = dme.read_byte(0x803C4CC6)
    curr_shards = curr_shards | (1 << (shard_num - 1))
    dme.write_byte(0x803C4CC6, curr_shards)


def remove_triforce_shard(shard_num: int):
    shard_mask = map_byte ^ (1 << (shard_num - 1))
    curr_shards = dme.read_byte(0x803C4CC6)
    dme.write_byte(0x803C4CC6, (curr_shards ^ shard_mask))


def give_bottle():
    if WWR.curr_bottles == 4:
        return
    dme.write_byte((0x803C4C52 + WWR.curr_bottles), 0x50)
    WWR.curr_bottles += 1


def remove_bottle():
    if WWR.curr_bottles == 4:
        return
    dme.write_byte((0x803C4C52 + WWR.curr_bottles), 0xFF)
