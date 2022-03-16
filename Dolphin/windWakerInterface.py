import random

import dolphin_memory_engine as dme

import Dolphin.windWakerResources as WWR
from Model.config import Config

random_rupoors = Config.get_config().Random_Rupoors

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
    return [(0xFF & read_word(0x803FED40)), (0xFF & read_word(0x803FED44))]


def clear_chest_items():
    return [write_word(0x803FED40, 0x0000), write_word(0x803FED44, 0x0000)]


def give_item_by_value(item_id: int):
    if item_id in WWR.inventory_handling:
        give_inventory_item_by_value(item_id)

    elif item_id in WWR.rupees:
        give_rupees(WWR.rupee_map[item_id])

    elif item_id in WWR.progressive_items:
        map_list = WWR.progressive_items_map[item_id]
        toggle_generic_progressive_item(map_list[0], map_list[1], map_list[2], True)

    elif item_id in WWR.shards_statues_wallets_and_songs:
        map_list = WWR.shards_statues_wallets_and_songs_map[item_id]
        toggle_bit_flag(map_list[0], map_list[1], True)

    elif item_id in WWR.progressive_consumables:
        map_list = WWR.progressive_consumables_map[item_id]
        upgrade_progressive_consumable(map_list[0], map_list[1])

    elif item_id in WWR.pearls:
        give_pearl(item_id)
    elif item_id in WWR.delivery_bag_items:
        give_delivery_bag_item(item_id)
    elif item_id in WWR.drc_dungeon_items:
        give_drc_item(item_id)
    elif item_id in WWR.fw_dungeon_items:
        give_fw_item(item_id)
    elif item_id in WWR.totg_dungeon_items:
        give_totg_item(item_id)
    elif item_id in WWR.ff_dungeon_items:
        give_ff_item(item_id)
    elif item_id in WWR.et_dungeon_items:
        give_et_item(item_id)
    elif item_id in WWR.wt_dungeon_items:
        give_wt_item(item_id)
    elif item_id in WWR.charts:
        give_map_by_id(item_id)
    elif item_id == 0x08:
        give_heart_container()
    elif item_id == 0x07:
        give_heart_pieces(1)
    elif item_id == 0x50:
        give_bottle()
    elif item_id == 0x28:
        give_power_bracelets()
    elif item_id == 0x43:
        give_heros_charm()
    elif item_id == 0xB2:
        give_magic_upgade()
    elif item_id == 0xAA:
        give_hurricane_spin()
    else:
        pass


def give_inventory_item_by_value(item: int):
    write_byte(WWR.player_inventory[item], item)
    item_name = WWR.item_name_dict[item]
    if item_name in WWR.single_bit_own_flag.keys():
        write_byte(WWR.single_bit_own_flag[item], 0x01)


def remove_inventory_item_by_value(item: int):
    write_byte(WWR.player_inventory[item], 0xFF)
    item_name = WWR.item_name_dict[item]
    if item_name in WWR.single_bit_own_flag.keys():
        write_byte(WWR.single_bit_own_flag[item], 0x00)


def give_item_by_name(item: str):
    give_inventory_item_by_value(WWR.item_id_dict[item])


def give_power_bracelets():
    dme.write_byte(0x803C4C18, 0x28)
    dme.write_byte(0x803C4CBE, 0x01)


def remove_power_bracelets():
    dme.write_byte(0x803C4C18, 0xFF)
    dme.write_byte(0x803C4CBE, 0x00)


def give_map_by_id(item_id: int):
    mapping = WWR.chart_mapping[item_id]
    curr_val = dme.read_word(mapping[0])
    dme.write_word(mapping[0], (curr_val | mapping[1]))


def take_map_by_id(item_id: int):
    mapping = WWR.chart_mapping[item_id]
    mask = 0xFFFFFFFF
    curr_val = dme.read_word(mapping[0])
    dme.write_word(mapping[0], (curr_val & (mask ^ mapping[1])))


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
    if random_rupoors and bool(random.getrandbits(1)):
        amount = ((amount ^ 0xFFFFFFFF) + 1)
    dme.write_word(0x803CA768, amount)

def write_byte_and_toggle_flag(address: int, value: int, flag_address: int, flag_offset: int, enable: bool):
    dme.write_byte(address, value)
    toggle_bit_flag(flag_address, flag_offset, enable)

def upgrade_progressive_consumable(max_address, curr_amount_address):
    curr_max = dme.read_byte(max_address)
    if curr_max == 30:
        dme.write_byte(max_address, 60)
        dme.write_byte(curr_amount_address, 60)
    elif curr_max == 60:
        dme.write_byte(max_address, 99)
        dme.write_byte(curr_amount_address, 99)
    elif curr_max == 99:
        return
    else:
        raise RuntimeWarning(f"Unexpected Value {curr_max} for address {max_address}")


def downgrade_progressive_consumable(max_address, curr_amount_address):
    curr_max = dme.read_byte(max_address)
    if curr_max == 99:
        dme.write_byte(max_address, 60)
        dme.write_byte(curr_amount_address, 60)
    elif curr_max == 60:
        dme.write_byte(max_address, 30)
        dme.write_byte(curr_amount_address, 30)
    elif curr_max == 30:
        return
    else:
        raise RuntimeWarning(f"Unexpected Value {curr_max} for address {max_address}")


def give_triforce_shard(shard_num: int):
    toggle_bit_flag(0x803C4CC6, (shard_num - 1), True)

def remove_triforce_shard(shard_num: int):
    toggle_bit_flag(0x803C4CC6, (shard_num - 1), False)


def give_delivery_bag_item(item_id: int):
    open_index = free_index(0x803C4C8E, 9)
    if open_index < 0:
        print(f"Error Adding {item_id} to the delivery bag")
        return
    dme.write_byte((0x803C4C8E + open_index), item_id)

def take_delivery_bag_item(item_id: int):
    target_index = find_val_in_list(0x803C4C8E, 9, item_id)
    if target_index < 0:
        return
    dme.write_byte((0x803C4C8E + target_index), 0xFF)


def give_bottle():
    open_index = free_index(0x803C4C52, 4)
    if open_index < 0:
        return
    dme.write_byte((0x803C4C52 + open_index), 0x50)


def remove_bottle():
    open_index = free_index(0x803C4C52, 4)
    if open_index <= 0:
        return
    dme.write_byte((0x803C4C52 + (open_index - 1)), 0xFF)


def free_index(starting_address: int, amount: int):
    return find_val_in_list(starting_address, amount, 0xFF)

def find_val_in_list(starting_address:int, amount: int, target_val: int):
    for index, value in enumerate(dme.read_bytes(starting_address, amount)):
        if value == target_val:
            return index
    return -1


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
        toggle_bit_flag(0x803C524A, 6, True)

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
        toggle_bit_flag(0x803C524A, 6, False)

def give_magic_upgade():
    dme.write_byte(0x803C4C1B, 0x20)
    dme.write_byte(0x803C4C1C, 0x20)

def take_magic_upgade():
    dme.write_byte(0x803C4C1B, 0x10)

def give_hurricane_spin():
    dme.write_byte(0x803C5295, 1)

def take_hurricane_spin():
    dme.write_byte(0x803C5295, 0)

def give_heros_charm():
    toggle_bit_flag(0x803C4CC0, 1, True)

def take_heros_charm():
    toggle_bit_flag(0x803C4CC0, 1, False)

def give_small_key_by_stage_id(stage_id: int):
    curr_stage_id = dme.read_byte(0x803C53A4)
    if curr_stage_id != stage_id:
        stage_mem_loc = WWR.stage_id_memory_locations[stage_id]
        curr_keys = dme.read_byte(stage_mem_loc + 0x20)
        dme.write_byte(stage_mem_loc + 0x20, curr_keys + 1)
    else:
        dme.write_bytes(0x803CA77C, b'\x00\x01')

def take_small_key_by_stage_id(stage_id: int):
    curr_stage_id = dme.read_byte(0x803C53A4)
    if curr_stage_id != stage_id:
        stage_mem_loc = WWR.stage_id_memory_locations[stage_id]
        curr_keys = dme.read_byte(stage_mem_loc + 0x20)
        if curr_keys > 0:
            dme.write_byte(stage_mem_loc + 0x20, curr_keys - 1)
    else:
        dme.write_bytes(0x803CA77C, b'\xFF\xFF')


def toggle_dungeon_map(stage_id: int):
    toggle_dungeon_flag(stage_id, 0)

def toggle_dungeon_compass(stage_id: int):
    toggle_dungeon_flag(stage_id, 1)

def toggle_dungeon_bk(stage_id: int):
    toggle_dungeon_flag(stage_id, 2)

def toggle_dungeon_flag(stage_id: int, offset: int):
    curr_stage_id = dme.read_byte(0x803C53A4)
    if curr_stage_id != stage_id:
        stage_mem_loc = WWR.stage_id_memory_locations[stage_id]
        toggle_bit_flag(stage_mem_loc + 0x21, offset, True)
    else:
        stage_mem_loc = WWR.stage_id_memory_locations[0x10] # Currently, Loaded Stage Location
        toggle_bit_flag(stage_mem_loc + 0x21, offset, True)

def give_drc_item(item_id: int):
    if item_id == 0x13:
        give_small_key_by_stage_id(3)
    elif item_id == 0x14:
        toggle_dungeon_bk(3)
    elif item_id == 0x1B:
        toggle_dungeon_map(3)
    elif item_id == 0x1C:
        toggle_dungeon_compass(3)
    else:
        return

def give_fw_item(item_id: int):
    if item_id == 0x1D:
        give_small_key_by_stage_id(4)
    elif item_id == 0x40:
        toggle_dungeon_bk(4)
    elif item_id == 0x41:
        toggle_dungeon_map(4)
    elif item_id == 0x5A:
        toggle_dungeon_compass(4)
    else:
        return

def give_totg_item(item_id: int):
    if item_id == 0x5B:
        give_small_key_by_stage_id(5)
    elif item_id == 0x5C:
        toggle_dungeon_bk(5)
    elif item_id == 0x5D:
        toggle_dungeon_map(5)
    elif item_id == 0x5E:
        toggle_dungeon_compass(5)
    else:
        return


def give_ff_item(item_id: int):
    if item_id == 0x5F:
        toggle_dungeon_map(2)
    elif item_id == 0x60:
        toggle_dungeon_compass(2)
    else:
        return



def give_et_item(item_id: int):
    if item_id == 0x73:
        give_small_key_by_stage_id(6)
    elif item_id == 0x74:
        toggle_dungeon_bk(6)
    elif item_id == 0x75:
        toggle_dungeon_map(6)
    elif item_id == 0x76:
        toggle_dungeon_compass(6)
    else:
        return


def give_wt_item(item_id: int):
    if item_id == 0x77:
        give_small_key_by_stage_id(7)
    elif item_id == 0x81:
        toggle_dungeon_bk(7)
    elif item_id == 0x84:
        toggle_dungeon_map(7)
    elif item_id == 0x85:
        toggle_dungeon_compass(7)
    else:
        return

def give_heart_container():
    give_heart_pieces(4)

def give_heart_pieces(amount: int):
    #Actual Location is 803CA77E with a Width of 2
    dme.write_byte(0x803CA77F, amount)


def toggle_generic_progressive_item(progressive_list: list[int], source_address: int, flag_address: int, enable: bool):
    curr_val = dme.read_byte(source_address)
    for index, value in enumerate(progressive_list):
        if value == curr_val and index != len(progressive_list) - 1:
            write_byte_and_toggle_flag(source_address, progressive_list[index + 1], flag_address, (index + 1), enable)

def toggle_bit_flag(address: int, offset: int, enable: bool):
    curr_val = dme.read_byte(address)
    bit_offset = 1 << offset
    masked_val = curr_val & bit_offset
    if not bool(masked_val) and enable:
       dme.write_byte(address, (curr_val ^ bit_offset))
    elif bool(masked_val) and not enable:
        dme.write_byte(address, (curr_val ^ bit_offset))



def check_valid_state():
    curr_val = dme.read_bytes(0x803C9D3C, 8)
    return curr_val == b'Name\x00\x00\x00\x00' or curr_val == b'sea_T\x00\x00\x00'

