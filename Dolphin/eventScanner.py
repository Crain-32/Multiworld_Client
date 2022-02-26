import asyncio

import dolphin_memory_engine as dme
from Dolphin.windWakerResources import stage_id_list as stage_map
from Model.config import Config



stage_flag_list = [[0 for inner_index in range(0x23)] for index in range(0x10)]

autofill_options = {
    0: "Chest",
    1: "Event",
    2: "Item Pickup",
    3: "Visited Rooms",
    4: "Unknown Type"
}

treasure_flags = list(range(0x0, 0x4))
mem_flags = list(range(0x4, 0x14))
item_flags = list(range(0x14, 0x18))
room_flags = list(range(0x18, 0x20))
dungeon_item_flags = list(range(0x20, 0x21))

scan_treasure = Config.get_config().Scan_Treasure
scan_event_flags = Config.get_config().Scan_Event_Flags
scan_item_flags = Config.get_config().Scan_Item_Flags
scan_dungeon_rooms = Config.get_config().Scan_Dungeon_Rooms


async def watch_changes():
    curr_stage_id = dme.read_byte(0x803C53A4)
    if curr_stage_id not in range(0xF):
        return
    in_game_vals = list(dme.read_bytes(0x803C5380, 0x23))
    curr_stage_vals = stage_flag_list[curr_stage_id]

    for index, val in enumerate(in_game_vals):
        val_difference = val ^ curr_stage_vals[index]
        if val_difference == 0:
            continue

        if index in dungeon_item_flags:
            continue
        elif index in treasure_flags and scan_treasure:
            handle_bits_in_byte_val(curr_stage_id, index, val_difference, 0)
        elif index in mem_flags and scan_event_flags:
            handle_bits_in_byte_val(curr_stage_id, index, val_difference, 1)
        elif index in item_flags and scan_item_flags:
            handle_bits_in_byte_val(curr_stage_id, index, val_difference, 2)
        elif index in room_flags and scan_dungeon_rooms:
            handle_bits_in_byte_val(curr_stage_id, index, val_difference, 3)
        else:
            handle_bits_in_byte_val(curr_stage_id, index, val_difference, 4)

    stage_flag_list[curr_stage_id] = in_game_vals
    await asyncio.sleep(1)


def handle_bits_in_byte_val(curr_stage_id, index, difference, event_type):
    bit_index = 7
    while difference != 0:
        if difference & 1 == 1:
            stage_name = dme.read_bytes(0x803C9D3C, 0x8)
            stage_str = str(stage_name)[2:].split("\\")[0]
            room_num = dme.read_byte(0x803F6A78)
            print_bits_helper(curr_stage_id, index, bit_index, stage_str, room_num)

            flag_info = get_user_input(event_type)
            write_to_file(curr_stage_id, stage_str, index, bit_index, flag_info, room_num)

        bit_index -= 1
        difference = difference >> 1


def print_bits_helper(curr_stage_id, index, bit_index, stage_str, room_num):
    print(f"{stage_map[curr_stage_id]} flag at byte {index} for " +
          f"bit {bit_index} in Stage:{stage_str} and Room:{room_num}")


def get_user_input(input_type):
    print("Flag type shortcuts are A | C | E Or type in the Location matching the Tracker")
    result = input(f"Press enter to Autofill to {autofill_options[input_type]}")
    if len(result) == 0:
        result = autofill_options[input_type]
    elif result == "A" or result == "a":
        result = "Cutscene"
    elif result == "C" or result == "c":
        result = "Chest"
    elif result == "E" or result == "e":
        result = "Event"
    return result


def write_to_file(stage_id, stage_str, byte_index, bit_index, flag_info, room_num):
    with open("flag_info.txt", 'a') as output_file:
        output_file.write(f"Stage ID:{stage_map[stage_id]}, Byte Offset: {byte_index}, Bit Offset: {bit_index} " +
                          f"Stage Name: {stage_str}, Room Number: {room_num}, Flag Info: {flag_info}\n")
