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
        give_rupees(WWR.rupee_map[item])
    elif item in WWR.swords:
        upgrade_sword()
    elif item in WWR.shields:
        upgrade_shield()
    elif item in WWR.shards:
        give_triforce_shard(item & 0xF)
    elif item in WWR.wallets:
        upgrade_wallet()
    elif item in WWR.bows:
        upgrade_bow()
    elif item == 0x50:
        give_bottle()
    elif item == 0x28:
        give_power_bracelets()
    else:
        pass


def give_inventory_item_by_value(item: int):
    write_byte(WWR.player_inventory[WWR.item_name_dict[item]], item)
    item_name = WWR.item_name_dict[item]
    if item_name in WWR.toggle_bit_ownership.keys():
        write_byte(WWR.toggle_bit_ownership[item_name], 0x01)


def remove_inventory_item_by_value(item: int):
    write_byte(WWR.player_inventory[WWR.item_name_dict[item]], 0xFF)
    item_name = WWR.item_name_dict[item]
    if item_name in WWR.toggle_bit_ownership.keys():
        write_byte(WWR.toggle_bit_ownership[item_name], 0x00)


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


def upgrade_wallet():
    curr_val = dme.read_byte(0x803C4C1A)
    if curr_val == 2:
        pass
    dme.write_byte(0x803C4C1A, curr_val + 1)


def downgrade_wallet():
    curr_val = dme.read_byte(0x803C4C1A)
    if curr_val == 0:
        pass
    dme.write_byte(0x803C4C1A, curr_val - 1)


def give_rupees(amount: int):
    dme.write_word(0x803CA768, amount)


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


def upgrade_bow():
    bow_vals = [0x27, 0x35, 0x36]
    curr_val = dme.read_byte(0x803C4C50)
    next_bow_val = 0
    if curr_val == 0x27:
        next_bow_val = 1
    if curr_val == 0x35:
        next_bow_val = 2
    if curr_val == 0x36:
        pass
    dme.write_byte(0x803C4C50, bow_vals[next_bow_val])
    curr_val = dme.read_byte(0x803C4C65)
    dme.write_byte(0x803C4C65, (curr_val | (1 << next_bow_val)))


def downgrade_bow():
    bow_vals = [0x27, 0x35, 0x36, 0xFF]
    curr_val = dme.read_byte(0x803C4C50)
    next_bow_val = 0
    if curr_val == 0x27:
        next_bow_val = 3
    if curr_val == 0x35:
        next_bow_val = 0
    if curr_val == 0x36:
        next_bow_val = 1
    dme.write_byte(0x803C4C50, bow_vals[next_bow_val])
    curr_val = dme.read_byte(0x803C4C65)
    dme.write_byte(0x803C4C65, (curr_val | (1 << next_bow_val)))


def upgrade_shield():
    shield_list = [0x3B, 0x3C]
    curr_val = dme.read_byte(0x803C4C17)
    next_shield = -1
    if curr_val == 0xFF:
        next_shield = 0
    if curr_val == 0x3B:
        next_shield = 1
    if next_shield < 0:
        pass
    dme.write_byte(0x803C4C17, shield_list[next_shield])
    curr_val = dme.read_byte(0x803C4CBD)
    dme.write_byte(0x803C4CBD, (curr_val | 1 << next_shield))


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
    open_index = bottle_index()
    if open_index < 0:
        pass
    dme.write_byte((0x803C4C52 + open_index), 0x50)


def remove_bottle():
    open_index = bottle_index()
    if open_index <= 0:
        pass
    dme.write_byte((0x803C4C52 + (open_index - 1)), 0xFF)


def bottle_index():
    bottle_list = []
    bottle_list.append(dme.read_byte(0x803C4C52))
    bottle_list.append(dme.read_byte(0x803C4C53))
    bottle_list.append(dme.read_byte(0x803C4C54))
    bottle_list.append(dme.read_byte(0x803C4C55))
    for index, bottle in enumerate(bottle_list):
        if bottle == 0xFF:
            return index
    return -1

def give_song(item: int):
    curr_val = dme.read_byte(0x803C4CC5)
    song_index = 0
    if item != 0x6B:
        song_index = (item % 0x6C)
    dme.write_byte(0x803C4CC5, (curr_val | (1 << song_index)))


def take_song(item: int):
    curr_val = dme.read_byte(0x803C4CC5)
    song_index = 0
    if item != 0x6B:
        song_index = (item % 0x6C)
    dme.write_byte(0x803C4CC5, (curr_val ^ (1 << song_index)))


def give_pearl(item: int):
    curr_val = dme.read_byte(0x803C4CC7)
    pearl_index = 0
    if item == 0x6A:
        pearl_index = 1
    if item == 0x6B:
        pearl_index = 2
    curr_val = curr_val | (1 << pearl_index)
    dme.write_byte(0x803C4CC7, curr_val)
    if curr_val == 0x7:
        # Raise ToTG
        totg_flags = dme.read_byte(0x803C524A)
        dme.write_byte(0x803C524A, (totg_flags | 0x40))


def take_pearl(item: int):
    curr_val = dme.read_byte(0x803C4CC7)
    pearl_index = 0
    if item == 0x6A:
        pearl_index = 1
    if item == 0x6B:
        pearl_index = 2
    changed_val = curr_val ^ (1 << pearl_index)
    dme.write_byte(0x803C4CC7, changed_val)
    if curr_val == 0x7:
        # Raise ToTG
        totg_flags = dme.read_byte(0x803C524A)
        dme.write_byte(0x803C524A, (totg_flags ^ 0x40))


def check_menu():
    curr_val = dme.read_bytes(0x803C9D3C, 8)
    return curr_val == b'Name\x00\x00\x00\x00' or curr_val == b'sea_T\x00\x00\x00'

