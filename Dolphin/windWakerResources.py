
item_id_dict = {
    "Heart (Pickup)": 0x00,           # Not going to Support
    "Green Rupee": 0x01,              # Supported
    "Blue Rupee": 0x02,               # Supported
    "Yellow Rupee": 0x03,             # Supported
    "Red Rupee": 0x04,                # Supported
    "Purple Rupee": 0x05,             # Supported
    "Orange Rupee": 0x06,             # Supported
    "Piece of Heart": 0x07,           # Supported
    "Heart Container": 0x08,          # Supported
    "Small Magic Jar (Pickup)": 0x09, # Not Supported
    "Large Magic Jar (Pickup)": 0x0A, # Not Supported
    "5 Bombs (Pickup)": 0x0B,         # Mirrors Small Key Behavior?
    "10 Bombs (Pickup)": 0x0C,        # ^
    "20 Bombs (Pickup)": 0x0D,        # ^
    "30 Bombs (Pickup)": 0x0E,        # ^
    "Silver Rupee": 0x0F,             # Supported
    "10 Arrows (Pickup)": 0x10,       # Mirrors Small Key Behavior?
    "20 Arrows (Pickup)": 0x11,       # ^
    "30 Arrows (Pickup)": 0x12,       # ^
    "DRC Small Key": 0x13,            # Supported
    "DRC Big Key": 0x14,              # Supported
    "Small Key": 0x15,                # Not used
    "Fairy (Pickup)": 0x16,           # Not going to Support
    "Yellow Rupee (Joke Message)": 0x1A, # Not Randomized?
    "DRC Dungeon Map": 0x1B,          # Supported
    "DRC Dungeon Compass": 0x1C,      # Supported
    "FW Small Key": 0x1D,             # Supported
    "Three Hearts (Pickup)": 0x1E,    # Not going to Support, only Zelda Hearts
    "Joy Pendant": 0x1F,              # Not Supported
    "Telescope": 0x20,                # Supported
    "Tingle Tuner": 0x21,             # Supported
    "Wind Waker": 0x22,               # Supported (Not Randomized)
    "Picto Box": 0x23,                # Supported
    "Spoils Bag": 0x24,               # Supported
    "Grappling Hook": 0x25,           # Supported
    "Deluxe Picto Box": 0x26,         # Supported
    "Hero's Bow": 0x27,               # Supported
    "Power Bracelets": 0x28,          # Supported
    "Iron Boots": 0x29,               # Supported
    "Magic Armor": 0x2A,              # Supported
    "Bait Bag": 0x2C,                 # Supported
    "Boomerang": 0x2D,                # Supported
    "Hookshot": 0x2F,                 # Supported
    "Delivery Bag": 0x30,             # Supported
    "Bombs": 0x31,                    # Supported
    "Hero's Clothes": 0x32,           # Not going to Support
    "Skull Hammer": 0x33,             # Supported
    "Deku Leaf": 0x34,                # Supported
    "Fire and Ice Arrows": 0x35,      # Supported
    "Light Arrow": 0x36,              # Supported
    "Hero's New Clothes": 0x37,       # Not going to Support
    "Hero's Sword": 0x38,             # Supported
    "Master Sword (Powerless)": 0x39, # Supported
    "Master Sword (Half Power)": 0x3A,# Supported
    "Hero's Shield": 0x3B,            # Supported
    "Mirror Shield": 0x3C,            # Supported
    "Recovered Hero's Sword": 0x3D,   # Supported
    "Master Sword (Full Power)": 0x3E,# Supported
    "Piece of Heart (Alternate Message)": 0x3F,   # Not used in the Randomizer?
    "FW Big Key": 0x40,               # Supported
    "FW Dungeon Map": 0x41,           # Supported
    "Pirate's Charm": 0x42,           # Not Randomized
    "Hero's Charm": 0x43,             # Supported
    "Skull Necklace": 0x45,           # Mirrors Delivery Bag Behavior
    "Boko Baba Seed": 0x46,           # ^
    "Golden Feather": 0x47,           # ^
    "Knight's Crest": 0x48,           # ^
    "Red Chu Jelly": 0x49,            # ^
    "Green Chu Jelly": 0x4A,          # ^
    "Blue Chu Jelly": 0x4B,           # Edge Case due to Blue Chus and Event flags. 0.0.5?
    "Dungeon Map": 0x4C,              # Not used in the Randomizer
    "Compass": 0x4D,                  # Not used in the Randomizer
    "Big Key": 0x4E,                  # Not used in the Randomizer
    "Empty Bottle": 0x50,             # Supported
    "Red Potion": 0x51,               # Not going to Support
    "Green Potion": 0x52,             # Not going to Support
    "Blue Potion": 0x53,              # Not going to Support
    "Elixir Soup (1/2)": 0x54,        # Not going to Support
    "Elixir Soup": 0x55,              # Not going to Support
    "Bottled Water": 0x56,            # Not going to Support
    "Fairy in Bottle": 0x57,          # Not going to Support
    "Forest Firefly": 0x58,           # Not going to Support
    "Forest Water": 0x59,             # Not going to Support
    "FW Dungeon Compass": 0x5A,       # Supported
    "TotG Small Key": 0x5B,           # Supported
    "TotG Big Key": 0x5C,             # Supported
    "TotG Dungeon Map": 0x5D,         # Supported
    "TotG Dungeon Compass": 0x5E,     # Supported
    "FF Dungeon Map": 0x5F,           # Supported
    "FF Dungeon Compass": 0x60,       # Supported
    "Triforce Shard 1": 0x61,         # Supported
    "Triforce Shard 2": 0x62,         # Supported
    "Triforce Shard 3": 0x63,         # Supported
    "Triforce Shard 4": 0x64,         # Supported
    "Triforce Shard 5": 0x65,         # Supported
    "Triforce Shard 6": 0x66,         # Supported
    "Triforce Shard 7": 0x67,         # Supported
    "Triforce Shard 8": 0x68,         # Supported
    "Nayru's Pearl": 0x69,            # Supported
    "Din's Pearl": 0x6A,              # Supported
    "Farore's Pearl": 0x6B,           # Supported
    "Wind's Requiem": 0x6D,           # Supported
    "Ballad of Gales": 0x6E,          # Supported
    "Command Melody": 0x6F,           # Supported
    "Earth God's Lyric": 0x70,        # Supported
    "Wind God's Aria": 0x71,          # Supported
    "Song of Passing": 0x72,          # Supported
    "ET Small Key": 0x73,             # Supported
    "ET Big Key": 0x74,               # Supported
    "ET Dungeon Map": 0x75,           # Supported
    "ET Dungeon Compass": 0x76,       # Supported
    "WT Small Key": 0x77,             # Supported
    "Boat's Sail": 0x78,              # Not Randomized
    "Triforce Chart 1 got deciphered": 0x79,     # Memory Scan, or Translation Patch?
    "Triforce Chart 2 got deciphered": 0x7A,     # Memory Scan, or Translation Patch?
    "Triforce Chart 3 got deciphered": 0x7B,     # Memory Scan, or Translation Patch?
    "Triforce Chart 4 got deciphered": 0x7C,     # Memory Scan, or Translation Patch?
    "Triforce Chart 5 got deciphered": 0x7D,     # Memory Scan, or Translation Patch?
    "Triforce Chart 6 got deciphered": 0x7E,     # Memory Scan, or Translation Patch?
    "Triforce Chart 7 got deciphered": 0x7F,     # Memory Scan, or Translation Patch?
    "Triforce Chart 8 got deciphered": 0x80,     # Memory Scan, or Translation Patch?
    "WT Big Key": 0x81,               # Supported
    "All-Purpose Bait": 0x82,         # Mirror Delivery Bag Handling?
    "Hyoi Pear": 0x83,                # Mirror Delivery Bag Handling?
    "WT Dungeon Map": 0x84,           # Supported
    "WT Dungeon Compass": 0x85,       # Supported
    "Town Flower": 0x8C,              # Not going to Support
    "Sea Flower": 0x8D,               # Not going to Support
    "Exotic Flower": 0x8E,            # Not going to Support
    "Hero's Flag": 0x8F,              # Not going to Support
    "Big Catch Flag": 0x90,           # Not going to Support
    "Big Sale Flag": 0x91,            # Not going to Support
    "Pinwheel": 0x92,                 # Not going to Support
    "Sickle Moon Flag": 0x93,         # Not going to Support
    "Skull Tower Idol": 0x94,         # Not going to Support
    "Fountain Idol": 0x95,            # Not going to Support
    "Postman Statue": 0x96,           # Not going to Support
    "Shop Guru Statue": 0x97,         # Not going to Support
    "Father's Letter": 0x98,          # Not Randomized
    "Note to Mom": 0x99,              # Supported
    "Maggie's Letter": 0x9A,          # Supported
    "Moblin's Letter": 0x9B,          # Supported
    "Cabana Deed": 0x9C,              # Supported
    "Complimentary ID": 0x9D,         # Not Researched
    "Fill-Up Coupon": 0x9E,           # Usable using current Mailing system?
    "Legendary Pictograph": 0x9F,     # Not Randomized
    "Dragon Tingle Statue": 0xA3,     # 0.0.3
    "Forbidden Tingle Statue": 0XA4,  # 0.0.3
    "Goddess Tingle Statue": 0XA5,    # 0.0.3
    "Earth Tingle Statue": 0XA6,      # 0.0.3
    "Wind Tingle Statue": 0XA7,       # 0.0.3
    "Hurricane Spin": 0XAA,           # Not Researched
    "1000 Rupee Wallet": 0XAB,        # Supported
    "5000 Rupee Wallet": 0XAC,        # Supported
    "60 Bomb Bomb Bag": 0XAD,         # Not Researched
    "99 Bomb Bomb Bag": 0XAE,         # Not Researched
    "60 Arrow Quiver": 0XAF,          # Not Researched
    "99 Arrow Quiver": 0XB0,          # Not Researched
    "Magic Meter Upgrade": 0XB2,      # Need additional Handling
    "50 Rupees, reward for finding 1 Tingle Statue": 0XB3,       # Not going to Support
    "100 Rupees, reward for finding 2 Tingle Statues": 0XB4,     # Not going to Support
    "150 Rupees, reward for finding 3 Tingle Statues": 0XB5,     # Not going to Support
    "200 Rupees, reward for finding 4 Tingle Statues": 0XB6,     # Not going to Support
    "250 Rupees, reward for finding 5 Tingle Statues": 0XB7,     # Not going to Support
    "500 Rupees, reward for finding all Tingle Statues": 0XB8,   # Not Researched
    "Submarine Chart": 0XC2,         # Supported
    "Beedle's Chart": 0XC3,          # Supported
    "Platform Chart": 0XC4,          # Supported
    "Light Ring Chart": 0XC5,        # Supported
    "Secret Cave Chart": 0XC6,       # Supported
    "Sea Hearts Chart": 0XC7,        # Supported
    "Island Hearts Chart": 0XC8,     # Supported
    "Great Fairy Chart": 0XC9,       # Supported
    "Octo Chart": 0XCA,              # Supported
    "IN-credible Chart": 0XCB,       # Supported
    "Treasure Chart 7": 0XCC,        # Supported
    "Treasure Chart 27": 0XCD,       # Supported
    "Treasure Chart 21": 0XCE,       # Supported
    "Treasure Chart 13": 0XCF,       # Supported
    "Treasure Chart 32": 0XD0,       # Supported
    "Treasure Chart 19": 0XD1,       # Supported
    "Treasure Chart 41": 0XD2,       # Supported
    "Treasure Chart 26": 0XD3,       # Supported
    "Treasure Chart 8": 0XD4,        # Supported
    "Treasure Chart 37": 0XD5,       # Supported
    "Treasure Chart 25": 0XD6,       # Supported
    "Treasure Chart 17": 0XD7,       # Supported
    "Treasure Chart 36": 0XD8,       # Supported
    "Treasure Chart 22": 0XD9,       # Supported
    "Treasure Chart 9": 0XDA,        # Supported
    "Ghost Ship Chart": 0XDB,        # Supported
    "Tingle's Chart": 0XDC,          # Supported
    "Treasure Chart 14": 0XDD,       # Supported
    "Treasure Chart 10": 0XDE,       # Supported
    "Treasure Chart 40": 0XDF,       # Supported
    "Treasure Chart 3": 0XE0,        # Supported
    "Treasure Chart 4": 0XE1,        # Supported
    "Treasure Chart 28": 0XE2,       # Supported
    "Treasure Chart 16": 0XE3,       # Supported
    "Treasure Chart 18": 0XE4,       # Supported
    "Treasure Chart 34": 0XE5,       # Supported
    "Treasure Chart 29": 0XE6,       # Supported
    "Treasure Chart 1": 0XE7,        # Supported
    "Treasure Chart 35": 0XE8,       # Supported
    "Treasure Chart 12": 0XE9,       # Supported
    "Treasure Chart 6": 0XEA,        # Supported
    "Treasure Chart 24": 0XEB,       # Supported
    "Treasure Chart 39": 0XEC,       # Supported
    "Treasure Chart 38": 0XED,       # Supported
    "Treasure Chart 2": 0XEE,        # Supported
    "Treasure Chart 33": 0XEF,       # Supported
    "Treasure Chart 31": 0XF0,       # Supported
    "Treasure Chart 23": 0XF1,       # Supported
    "Treasure Chart 5": 0XF2,        # Supported
    "Treasure Chart 20": 0XF3,       # Supported
    "Treasure Chart 30": 0XF4,       # Supported
    "Treasure Chart 15": 0XF5,       # Supported
    "Treasure Chart 11": 0XF6,       # Supported
    "Triforce Chart 8": 0XF7,        # Supported
    "Triforce Chart 7": 0XF8,        # Supported
    "Triforce Chart 6": 0XF9,        # Supported
    "Triforce Chart 5": 0XFA,        # Supported
    "Triforce Chart 4": 0XFB,        # Supported
    "Triforce Chart 3": 0XFC,        # Supported
    "Triforce Chart 2": 0XFD,        # Supported
    "Triforce Chart 1": 0XFE,        # Supported
}
inventory_handling = [
    0x20,  # Telescope
    0x78,  # Sail
    0x22,  # Wind Waker
    0x25,  # Grappling Hook
    0x24,  # Spoils Bag
    0x21,  # Tingle Tuner
    0x29,  # Iron Boots
    0x2A,  # Magic Armor
    0x2C,  # Bait Bag
    0x2D,  # Boomerang
    0x34,  # Deku Leaf
    0x31,  # Bombs
    0x30,  # Delivery Bag
    0x2F,  # Hookshot
    0x33   # Skull Hammer
]
delivery_bag_items = [
    0x99,  # Note to Mom
    0x9A,  # Maggie's Letter
    0x9B,  # Moblin's Letter
    0x9C   # Cabana Deed
]
rupees = [
    0x01,  # Green
    0x02,  # Blue
    0x03,  # Yellow
    0x04,  # Red
    0x05,  # Purple
    0x06,  # Orange
    0x0F,  # Silver
    0xB8   # TREVOR
]
rupee_map = {
    0x01: 0x0001, # Green
    0x02: 0x0005, # Blue
    0x03: 0x000A, # Yellow
    0x04: 0x0014, # Red
    0x05: 0x0032, # Purple
    0x06: 0x0064, # Orange
    0x0F: 0x00C8, # Silver
    0xB8: 0x01F4  # TREVOR
}
curr_swords = 1
swords = [
    0x38,  # Hero's
    0x39,  # Master Sword
    0x3A,  # Half Power
    0x3E,  # Full Power
]
curr_shields = 0
shields = [
    0x3B,  # Hero's Shield
    0x3C   # Mirror Shield
]
shards = [
    0x61,  # Triforce Shard 1 - 8
    0x62,  # 2
    0x63,  # 3
    0x64,  # 4
    0x65,  # 5
    0x66,  # 6
    0x67,  # 7
    0x68   # 8
]
curr_bow = 0
bows = [
    0x27,  # Hero's
    0x35,  # Fire/Ice
    0x36   # Light Arrows
]
wallets = [
    0XAB,  # 1000
    0XAC   # 5000
]
songs = [
    0x6D,  # Wind's Requiem
    0x6E,  # Ballad of Gales
    0x6F,  # Command Melody
    0x70,  # Earth God's Lyric
    0x71,  # Wind God's Aria
    0x72   # Song of Passing
]
pearls = [
    0x69,  # Nayru's Pearl
    0x6A,  # Din's Pearl
    0x6B   # Farore's Pearl
]
pictos = [
    0x23,  # Picto Box
    0x26   # Deluxe Picto Box
]
charts = [
    0XC2, # "Submarine Chart":
    0XC3, # "Beedle's Chart":
    0XC4, # "Platform Chart":
    0XC5, # "Light Ring Chart":
    0XC6, # "Secret Cave Chart":
    0XC7, # "Sea Hearts Chart":
    0XC8, # "Island Hearts Chart":
    0XC9, # "Great Fairy Chart":
    0XCA, # "Octo Chart":
    0XCB, # "IN-credible Chart":
    0XCC, # "Treasure Chart 7":
    0XCD, # "Treasure Chart 27":
    0XCE, # "Treasure Chart 21":
    0XCF, # "Treasure Chart 13":
    0XD0, # "Treasure Chart 32":
    0XD1, # "Treasure Chart 19":
    0XD2, # "Treasure Chart 41":
    0XD3, # "Treasure Chart 26":
    0XD4, # "Treasure Chart 8":
    0XD5, # "Treasure Chart 37":
    0XD6, # "Treasure Chart 25":
    0XD7, # "Treasure Chart 17":
    0XD8, # "Treasure Chart 36":
    0XD9, # "Treasure Chart 22":
    0XDA, # "Treasure Chart 9":
    0XDB, # "Ghost Ship Chart":
    0XDC, # "Tingle's Chart":
    0XDD, # "Treasure Chart 14":
    0XDE, # "Treasure Chart 10":
    0XDF, # "Treasure Chart 40":
    0XE0, # "Treasure Chart 3":
    0XE1, # "Treasure Chart 4":
    0XE2, # "Treasure Chart 28":
    0XE3, # "Treasure Chart 16":
    0XE4, # "Treasure Chart 18":
    0XE5, # "Treasure Chart 34":
    0XE6, # "Treasure Chart 29":
    0XE7, # "Treasure Chart 1":
    0XE8, # "Treasure Chart 35":
    0XE9, # "Treasure Chart 12":
    0XEA, # "Treasure Chart 6":
    0XEB, # "Treasure Chart 24":
    0XEC, # "Treasure Chart 39":
    0XED, # "Treasure Chart 38":
    0XEE, # "Treasure Chart 2":
    0XEF, # "Treasure Chart 33":
    0XF0, # "Treasure Chart 31":
    0XF1, # "Treasure Chart 23":
    0XF2, # "Treasure Chart 5":
    0XF3, # "Treasure Chart 20":
    0XF4, # "Treasure Chart 30":
    0XF5, # "Treasure Chart 15":
    0XF6, # "Treasure Chart 11":
    0XF7, # "Triforce Chart 8":
    0XF8, # "Triforce Chart 7":
    0XF9, # "Triforce Chart 6":
    0XFA, # "Triforce Chart 5":
    0XFB, # "Triforce Chart 4":
    0XFC, # "Triforce Chart 3":
    0XFD, # "Triforce Chart 2":
    0XFE  # "Triforce Chart 1":
]
tingle_statues = [
    0xA3,   # Dragon Tingle Statue
    0XA4,   # Forbidden Tingle Statue
    0XA5,   # Goddess Tingle Statue
    0XA6,   # Earth Tingle Statue
    0XA7    # Wind Tingle Statue
]
quivers = [
    0xAF,  # 60 Quiver
    0xB0   # 99 Quiver
]
bomb_bags = [
    0xAD,  # 60 Bomb Bag
    0xAE  # 99 Bomb Bag
]

logical_items = {
    0x20: False,  # Telescope
    0x78: False,  # Sail
    0x22: False,  # Wind Waker
    0x25: False,  # Grappling Hook
    0x21: False,  # Tingle Tuner
    0x29: False,  # Iron Boots
    0x2A: False,  # Magic Armor
    0x2D: False,  # Boomerang
    0x34: False,  # Deku Leaf
    0x31: False,  # Bombs
    0x2F: False,  # Hookshot
    0x33: False,  # Skull Hammer
    0x61: False,  # Triforce Shard 1 - 8
    0x62: False,
    0x63: False,
    0x64: False,
    0x65: False,
    0x66: False,
    0x67: False,
    0x68: False,
    0x28: False   # Power Bracelets
}

map_byte = 0xFF
curr_bottles = 0

###
#
###
drc_stage_id = 3
drc_dungeon_items = [
    0x13, # Small Key
    0x14, # Big Key
    0x1B, # Map
    0x1C  # Compass
]

fw_stage_id = 4
fw_dungeon_items = [
    0x1D, # Small Key
    0x40, # Big Key
    0x41, # Map
    0x5A  # Compass
]

totg_stage_id = 5
totg_dungeon_items = [
    0x5B, # Small Key
    0x5C, # Big Key
    0x5D, # Map
    0x5E  # Compass
]

ff_stage_id = 2 # Maybe Not? Need to test
ff_dungeon_items = [
    0x5F, # Map
    0x60  # Compass
]

et_stage_id = 6
et_dungeon_items = [
    0x73, # Small Key
    0x74, # Big Key
    0x75, # Map
    0x76  # Compass
]

wt_stage_id = 7
wt_dungeon_items = [
    0x77, # Small Key
    0x81, # Big Key
    0x84, # Map
    0x85  # Compass
]

item_name_dict = {v: k for k, v in item_id_dict.items()}
"""
2B 2E 44 4F 
6C 86 87 88 
89 8A 8B A0 
A1 A2 A8 A9 
B1 B9 BA BB 
BC BD BE BF 
C0 C1
29 Open Item Ids.
"""

# https://github.com/LagoLunatic/WW-Hacking-Docs/blob/0abf443d0a81dde6a1d42f849fd8fd4fbe534c82/RAM%20Map.txt#L536
player_inventory = {
    0x20: 0x803C4C44, # Telescope
    0x78: 0x803C4C45, # Sail
    0x22: 0x803C4C46, # Wind Waker
    0x25: 0x803C4C47, # Grappling Hook
    0x24: 0x803C4C48, # Spoils Bag
    0x2D: 0x803C4C49, # Boomerang
    0x34: 0x803C4C4A, # Deku Leaf
    0x21: 0x803C4C4B, # Tingle Tuner
    0x23: 0x803C4C4C, # Picto Box
    0x26: 0x803C4C4C, # Deluxe Picto Box
    0x29: 0x803C4C4D, # Iron Boots
    0x2A: 0x803C4C4E, # Magic Armor
    0x2C: 0x803C4C4F, # Bait Bag
    0x27: 0x803C4C50, # Hero's Bow
    0x35: 0x803C4C50, # Fire/Ice
    0x36: 0x803C4C50, # Light Arrows
    0x31: 0x803C4C51, # Bombs
    0x50: 0x803C4C52, # Empty Bottle, 0x803C4C52 - 0x803C4C55
    0x30: 0x803C4C56, # Delivery Bag
    0x2F: 0x803C4C57, # Hookshot
    0x33: 0x803C4C58  # Skull Hammer
}

useful_address = {
    "Add Rupees": 0x803CA768
}

misc_memory_location = {
    "current_b_button": 0x803C4C16,
    "current_shield": 0x803C4C17,
    "power_bracelet_status": 0x803C4C18,
    "current_wallet": 0x803C4C1A
}

single_bit_own_flag = {
    0x25: 0x803C4C5C, # Grappling Hook
    0x24: 0x803C4C5D, # Spoils Bag
    0x2D: 0x803C4C5E, # Boomerang
    0x34: 0x803C4C5F, # Deku Leaf
    0x21: 0x803C4C5F, # Tingle Tuner
    0x29: 0x803C4C62, # Iron boot
    0x2A: 0x803C4C63, # Magic Armor
    0x2C: 0x803C4C64, # Bait Bag
    0x31: 0x803C4C66, # Bombs
    0x30: 0x803C4C6B, # Delivery Bag
    0x2F: 0x803C4C6C, # Hookshot
    0x33: 0x803C4C6D, # Skull Hammer
    0x28: 0x803C4CBE  # Power Bracelets
}
stage_id_list = {
    0x0: "Sea",
    0x1: "Sea Alt",
    0x2: "Forsaken Fortress",
    0x3: "Dragon Roost Cavern",
    0x4: "Forbidden Woods",
    0x5: "Tower of the Gods",
    0x6: "Earth Temple",
    0x7: "Wind Temple",
    0x8: "Ganon's Tower",
    0x9: "Hyrule",
    0xA: "Ship Interiors",
    0xB: "Hours and Misc Places",
    0xC: "Cave Interiors",
    0xD: "More Cave Interiors & Ship Interiors",
    0xE: "Blue Chus",
    0xF: "Test Maps"
}
stage_id_memory_locations = {
    0x0: 0x803C4F88,
    0x1: 0x803C4FAC,
    0x2: 0x803C4FD0,
    0x3: 0x803C4FF4,
    0x4: 0x803C5018,
    0x5: 0x803C503C,
    0x6: 0x803C5060,
    0x7: 0x803C5084,
    0x8: 0x803C50A8,
    0x9: 0x803C50CC,
    0xA: 0x803C50F0,
    0xB: 0x803C5114,
    0xC: 0x803C5138,
    0xD: 0x803C515C,
    0xE: 0x803C5180,
    0xF: 0x803C51A4,
    0x10: 0x803C5380 # Current Loaded Stage Info
}
chart_mapping = {
    0XC2:[0x803C4CE0 ,0x10000000], # "Submarine Chart":
    0XC3:[0x803C4CE0 ,0x08000000], # "Beedle's Chart":
    0XC4:[0x803C4CE0 ,0x04000000], # "Platform Chart":
    0XC5:[0x803C4CE0 ,0x02000000], # "Light Ring Chart":
    0XC6:[0x803C4CE0 ,0x01000000], # "Secret Cave Chart":
    0XC7:[0x803C4CE0 ,0x00800000], # "Sea Hearts Chart":
    0XC8:[0x803C4CE0 ,0x00400000], # "Island Hearts Chart":
    0XC9:[0x803C4CE0 ,0x00200000], # "Great Fairy Chart":
    0XCA:[0x803C4CE0 ,0x00100000], # "Octo Chart":
    0XCB:[0x803C4CE0 ,0x00080000], # "IN-credible Chart":
    0XCC:[0x803C4CE0 ,0x00040000], # "Treasure Chart 7":
    0XCD:[0x803C4CE0 ,0x00020000], # "Treasure Chart 27":
    0XCE:[0x803C4CE0 ,0x00010000], # "Treasure Chart 21":
    0XCF:[0x803C4CE0 ,0x00008000], # "Treasure Chart 13":
    0XD0:[0x803C4CE0 ,0x00004000], # "Treasure Chart 32":
    0XD1:[0x803C4CE0 ,0x00002000], # "Treasure Chart 19":
    0XD2:[0x803C4CE0 ,0x00001000], # "Treasure Chart 41":
    0XD3:[0x803C4CE0 ,0x00000800], # "Treasure Chart 26":
    0XD4:[0x803C4CE0 ,0x00000400], # "Treasure Chart 8":
    0XD5:[0x803C4CE0 ,0x00000200], # "Treasure Chart 37":
    0XD6:[0x803C4CE0 ,0x00000100], # "Treasure Chart 25":
    0XD7:[0x803C4CE0 ,0x00000080], # "Treasure Chart 17":
    0XD8:[0x803C4CE0 ,0x00000040], # "Treasure Chart 36":
    0XD9:[0x803C4CE0 ,0x00000020], # "Treasure Chart 22":
    0XDA:[0x803C4CE0 ,0x00000010], # "Treasure Chart 9":
    0XDB:[0x803C4CE0 ,0x00000008], # "Ghost Ship Chart":
    0XDC:[0x803C4CE0 ,0x00000004], # "Tingle's Chart":
    0XDD:[0x803C4CE0 ,0x00000002], # "Treasure Chart 14":
    0XDE:[0x803C4CE0 ,0x00000001], # "Treasure Chart 10":
    0XDF:[0x803C4CDC ,0x80000000], # "Treasure Chart 40":
    0XE0:[0x803C4CDC ,0x40000000], # "Treasure Chart 3":
    0XE1:[0x803C4CDC ,0x20000000], # "Treasure Chart 4":
    0XE2:[0x803C4CDC ,0x10000000], # "Treasure Chart 28":
    0XE3:[0x803C4CDC ,0x08000000], # "Treasure Chart 16":
    0XE4:[0x803C4CDC ,0x04000000], # "Treasure Chart 18":
    0XE5:[0x803C4CDC ,0x02000000], # "Treasure Chart 34":
    0XE6:[0x803C4CDC ,0x01000000], # "Treasure Chart 29":
    0XE7:[0x803C4CDC ,0x00800000], # "Treasure Chart 1":
    0XE8:[0x803C4CDC ,0x00400000], # "Treasure Chart 35":
    0XE9:[0x803C4CDC ,0x00200000], # "Treasure Chart 12":
    0XEA:[0x803C4CDC ,0x00100000], # "Treasure Chart 6":
    0XEB:[0x803C4CDC ,0x00080000], # "Treasure Chart 24":
    0XEC:[0x803C4CDC ,0x00040000], # "Treasure Chart 39":
    0XED:[0x803C4CDC ,0x00020000], # "Treasure Chart 38":
    0XEE:[0x803C4CDC ,0x00010000], # "Treasure Chart 2":
    0XEF:[0x803C4CDC ,0x00008000], # "Treasure Chart 33":
    0XF0:[0x803C4CDC ,0x00004000], # "Treasure Chart 31":
    0XF1:[0x803C4CDC ,0x00002000], # "Treasure Chart 23":
    0XF2:[0x803C4CDC ,0x00001000], # "Treasure Chart 5":
    0XF3:[0x803C4CDC ,0x00000800], # "Treasure Chart 20":
    0XF4:[0x803C4CDC ,0x00000400], # "Treasure Chart 30":
    0XF5:[0x803C4CDC ,0x00000200], # "Treasure Chart 15":
    0XF6:[0x803C4CDC ,0x00000100], # "Treasure Chart 11":
    0XF7:[0x803C4CDC ,0x00000080], # "Triforce Chart 8":
    0XF8:[0x803C4CDC ,0x00000040], # "Triforce Chart 7":
    0XF9:[0x803C4CDC ,0x00000020], # "Triforce Chart 6":
    0XFA:[0x803C4CDC ,0x00000010], # "Triforce Chart 5":
    0XFB:[0x803C4CDC ,0x00000008], # "Triforce Chart 4":
    0XFC:[0x803C4CDC ,0x00000004], # "Triforce Chart 3":
    0XFD:[0x803C4CDC ,0x00000002], # "Triforce Chart 2":
    0XFE:[0x803C4CDC ,0x00000001], # "Triforce Chart 1":
}
statue_mapping = {
    0xA3: [0x803C5296, 0x04],  # Dragon Tingle Statue
    0XA4: [0x803C5296, 0x08],  # Forbidden Tingle Statue
    0XA5: [0x803C5296, 0x10],  # Goddess Tingle Statue
    0XA6: [0x803C5296, 0x20],  # Earth Tingle Statue
    0XA7: [0x803C5296, 0x40]   # Wind Tingle Statue
}
"""
  Bottle item IDs:
    50 - Empty Bottle
    51 - Red Potion
    52 - Green Potion
    53 - Blue Potion
    54 - Elixir Soup (1/2)
    55 - Elixir Soup
    56 - Bottled Water
    57 - Fairy in Bottle
    58 - Forest Firefly
    59 - Forest Water
"""
