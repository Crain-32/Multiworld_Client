import itertools

item_id_dict = {
    "Heart (Pickup)": 0x00,
    "Green Rupee": 0x01,
    "Blue Rupee": 0x02,
    "Yellow Rupee": 0x03,
    "Red Rupee": 0x04,
    "Purple Rupee": 0x05,
    "Orange Rupee": 0x06,
    "Piece of Heart": 0x07,
    "Heart Container": 0x08,
    "Small Magic Jar (Pickup)": 0x09,
    "Large Magic Jar (Pickup)": 0x0A,
    "5 Bombs (Pickup)": 0x0B,
    "10 Bombs (Pickup)": 0x0C,
    "20 Bombs (Pickup)": 0x0D,
    "30 Bombs (Pickup)": 0x0E,
    "Silver Rupee": 0x0F,
    "10 Arrows (Pickup)": 0x10,
    "20 Arrows (Pickup)": 0x11,
    "30 Arrows (Pickup)": 0x12,
    "Small Key": 0x15,
    "Fairy (Pickup)": 0x16,
    "Yellow Rupee (Joke Message)": 0x1A,
    "Three Hearts (Pickup)": 0x1E,
    "Joy Pendant": 0x1F,
    "Telescope": 0x20,
    "Tingle Tuner": 0x21,
    "Wind Waker": 0x22,
    "Picto Box": 0x23,
    "Spoils Bag": 0x24,
    "Grappling Hook": 0x25,
    "Deluxe Picto Box": 0x26,
    "Hero's Bow": 0x27,
    "Power Bracelets": 0x28,
    "Iron Boots": 0x29,
    "Magic Armor": 0x2A,
    "Bait Bag": 0x2C,
    "Boomerang": 0x2D,
    "Hookshot": 0x2F,
    "Delivery Bag": 0x30,
    "Bombs": 0x31,
    "Hero's Clothes": 0x32,
    "Skull Hammer": 0x33,
    "Deku Leaf": 0x34,
    "Fire and Ice Arrows": 0x35,
    "Light Arrow": 0x36,
    "Hero's New Clothes": 0x37,
    "Hero's Sword": 0x38,
    "Master Sword (Powerless)": 0x39,
    "Master Sword (Half Power)": 0x3A,
    "Hero's Shield": 0x3B,
    "Mirror Shield": 0x3C,
    "Recovered Hero's Sword": 0x3D,
    "Master Sword (Full Power)": 0x3E,
    "Piece of Heart (Alternate Message)": 0x3F,
    "Pirate's Charm": 0x42,
    "Hero's Charm": 0x43,
    "Skull Necklace": 0x45,
    "Boko Baba Seed": 0x46,
    "Golden Feather": 0x47,
    "Knight's Crest": 0x48,
    "Red Chu Jelly": 0x49,
    "Green Chu Jelly": 0x4A,
    "Blue Chu Jelly": 0x4B,
    "Dungeon Map": 0x4C,
    "Compass": 0x4D,
    "Big Key": 0x4E,
    "Empty Bottle": 0x50,
    "Red Potion": 0x51,
    "Green Potion": 0x52,
    "Blue Potion": 0x53,
    "Elixir Soup (1/2)": 0x54,
    "Elixir Soup": 0x55,
    "Bottled Water": 0x56,
    "Fairy in Bottle": 0x57,
    "Forest Firefly": 0x58,
    "Forest Water": 0x59,
    "Triforce Shard 1": 0x61,
    "Triforce Shard 2": 0x62,
    "Triforce Shard 3": 0x63,
    "Triforce Shard 4": 0x64,
    "Triforce Shard 5": 0x65,
    "Triforce Shard 6": 0x66,
    "Triforce Shard 7": 0x67,
    "Triforce Shard 8": 0x68,
    "Nayru's Pearl": 0x69,
    "Din's Pearl": 0x6A,
    "Farore's Pearl": 0x6B,
    "Wind's Requiem": 0x6D,
    "Ballad of Gales": 0x6E,
    "Command Melody": 0x6F,
    "Earth God's Lyric": 0x70,
    "Wind God's Aria": 0x71,
    "Song of Passing": 0x72,
    "Boat's Sail": 0x78,
    "Triforce Chart 1 got deciphered": 0x79,
    "Triforce Chart 2 got deciphered": 0x7A,
    "Triforce Chart 3 got deciphered": 0x7B,
    "Triforce Chart 4 got deciphered": 0x7C,
    "Triforce Chart 5 got deciphered": 0x7D,
    "Triforce Chart 6 got deciphered": 0x7E,
    "Triforce Chart 7 got deciphered": 0x7F,
    "Triforce Chart 8 got deciphered": 0x80,
    "All-Purpose Bait": 0x82,
    "Hyoi Pear": 0x83,
    "Town Flower": 0x8C,
    "Sea Flower": 0x8D,
    "Exotic Flower": 0x8E,
    "Hero's Flag": 0x8F,
    "Big Catch Flag": 0x90,
    "Big Sale Flag": 0x91,
    "Pinwheel": 0x92,
    "Sickle Moon Flag": 0x93,
    "Skull Tower Idol": 0x94,
    "Fountain Idol": 0x95,
    "Postman Statue": 0x96,
    "Shop Guru Statue": 0x97,
    "Father's Letter": 0x98,
    "Note to Mom": 0x99,
    "Maggie's Letter": 0x9A,
    "Moblin's Letter": 0x9B,
    "Cabana Deed": 0x9C,
    "Complimentary ID": 0x9D,
    "Fill-Up Coupon": 0x9E,
    "Legendary Pictograph": 0x9F,
    "Dragon Tingle Statue": 0xA3,
    "Forbidden Tingle Statue": 0XA4,
    "Goddess Tingle Statue": 0XA5,
    "Earth Tingle Statue": 0XA6,
    "Wind Tingle Statue": 0XA7,
    "Hurricane Spin": 0XAA,
    "1000 Rupee Wallet": 0XAB,
    "5000 Rupee Wallet": 0XAC,
    "60 Bomb Bomb Bag": 0XAD,
    "99 Bomb Bomb Bag": 0XAE,
    "60 Arrow Quiver": 0XAF,
    "99 Arrow Quiver": 0XB0,
    "Magic Meter Upgrade": 0XB2,
    "50 Rupees, reward for finding 1 Tingle Statue": 0XB3,
    "100 Rupees, reward for finding 2 Tingle Statues": 0XB4,
    "150 Rupees, reward for finding 3 Tingle Statues": 0XB5,
    "200 Rupees, reward for finding 4 Tingle Statues": 0XB6,
    "250 Rupees, reward for finding 5 Tingle Statues": 0XB7,
    "500 Rupees, reward for finding all Tingle Statues": 0XB8,
    "Submarine Chart": 0XC2,
    "Beedle's Chart": 0XC3,
    "Platform Chart": 0XC4,
    "Light Ring Chart": 0XC5,
    "Secret Cave Chart": 0XC6,
    "Sea Hearts Chart": 0XC7,
    "Island Hearts Chart": 0XC8,
    "Great Fairy Chart": 0XC9,
    "Octo Chart": 0XCA,
    "IN-credible Chart": 0XCB,
    "Treasure Chart 7": 0XCC,
    "Treasure Chart 27": 0XCD,
    "Treasure Chart 21": 0XCE,
    "Treasure Chart 13": 0XCF,
    "Treasure Chart 32": 0XD0,
    "Treasure Chart 19": 0XD1,
    "Treasure Chart 41": 0XD2,
    "Treasure Chart 26": 0XD3,
    "Treasure Chart 8": 0XD4,
    "Treasure Chart 37": 0XD5,
    "Treasure Chart 25": 0XD6,
    "Treasure Chart 17": 0XD7,
    "Treasure Chart 36": 0XD8,
    "Treasure Chart 22": 0XD9,
    "Treasure Chart 9": 0XDA,
    "Ghost Ship Chart": 0XDB,
    "Tingle's Chart": 0XDC,
    "Treasure Chart 14": 0XDD,
    "Treasure Chart 10": 0XDE,
    "Treasure Chart 40": 0XDF,
    "Treasure Chart 3": 0XE0,
    "Treasure Chart 4": 0XE1,
    "Treasure Chart 28": 0XE2,
    "Treasure Chart 16": 0XE3,
    "Treasure Chart 18": 0XE4,
    "Treasure Chart 34": 0XE5,
    "Treasure Chart 29": 0XE6,
    "Treasure Chart 1": 0XE7,
    "Treasure Chart 35": 0XE8,
    "Treasure Chart 12": 0XE9,
    "Treasure Chart 6": 0XEA,
    "Treasure Chart 24": 0XEB,
    "Treasure Chart 39": 0XEC,
    "Treasure Chart 38": 0XED,
    "Treasure Chart 2": 0XEE,
    "Treasure Chart 33": 0XEF,
    "Treasure Chart 31": 0XF0,
    "Treasure Chart 23": 0XF1,
    "Treasure Chart 5": 0XF2,
    "Treasure Chart 20": 0XF3,
    "Treasure Chart 30": 0XF4,
    "Treasure Chart 15": 0XF5,
    "Treasure Chart 11": 0XF6,
    "Triforce Chart 8": 0XF7,
    "Triforce Chart 7": 0XF8,
    "Triforce Chart 6": 0XF9,
    "Triforce Chart 5": 0XFA,
    "Triforce Chart 4": 0XFB,
    "Triforce Chart 3": 0XFC,
    "Triforce Chart 2": 0XFD,
    "Triforce Chart 1": 0XFE,
}
inventory_handling = [
    0x20,  # Telescope
    0x78,  # Sail
    0x22,  # Wind Waker
    0x25,  # Grappling Hook
    0x21,  # Tingle Tuner
    0x29,  # Iron Boots
    0x2A,  # Magic Armor
    0x2D,  # Boomerang
    0x34,  # Deku Leaf
    0x31,  # Bombs
    0x2F,  # Hookshot
    0x33  # Skull Hammer
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
    0x01: 0x0001,
    0x02: 0x0005,
    0x03: 0x000A,
    0x04: 0x0014,
    0x05: 0x0032,
    0x06: 0x0064,
    0x0F: 0x00C8,
    0xB8: 0x01F4
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
    0x62,
    0x63,
    0x64,
    0x65,
    0x66,
    0x67,
    0x68
]
curr_bow = 0
bows = [
    0x27,
    0x35,
    0x36
]
non_progressive_key_items = {
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
keylunacy_item_dictionary = {
    "DRC Small Key": 0x13,
    "DRC Big Key": 0x14,
    "DRC Dungeon Map": 0x1B,
    "DRC Compass": 0x1C,
    "FW Small Key": 0x1D,
    "FW Big Key": 0x40,
    "FW Dungeon Map": 0x41,
    "FW Compass": 0x5A,
    "TotG Small Key": 0x5B,
    "TotG Big Key": 0x5C,
    "TotG Dungeon Map": 0x5D,
    "TotG Compass": 0x5E,
    "FF Dungeon Map": 0x5F,
    "FF Compass": 0x60,
    "ET Small Key": 0x73,
    "ET Big Key": 0x74,
    "ET Dungeon Map": 0x75,
    "ET Compass": 0x76,
    "WT Small Key": 0x77,
    "WT Big Key": 0x81,
    "WT Dungeon Map": 0x84,
    "WT Compass": 0x85,
}

item_name_dict = {v: k for k, v in itertools.chain(item_id_dict.items(), keylunacy_item_dictionary.items())}
"""
Leftover Item Ids - Might come in handy, since they're always patched.
13 14 1B 1C (Keylunacy) 
1D 40 41 5A (Keylunacy)
5B 5C 5D 5E (Keylunacy)
5F 60 73 74 (Keylunacy)
75 76 77 81 (Keylunacy)
84 85       (Keylunacy)
22 Taken Ids.
-----------------------
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
    "Telescope": 0x803C4C44,
    "Sail": 0x803C4C45,
    "Wind Waker": 0x803C4C46,
    "Grappling Hook": 0x803C4C47,
    "Spoils Bag": 0x803C4C48,
    "Boomerang": 0x803C4C49,
    "Deku Leaf": 0x803C4C4A,
    "Tingle Tuner": 0x803C4C4B,
    "Picto Box": 0x803C4C4C,
    "Iron Boots": 0x803C4C4D,
    "Magic Armor": 0x803C4C4E,
    "Bait Bag": 0x803C4C4F,
    "Bow": 0x803C4C50,
    "Bombs": 0x803C4C51,
    "Bottle 1": 0x803C4C52,
    "Bottle 2": 0x803C4C53,
    "Bottle 3": 0x803C4C54,
    "Bottle 4": 0x803C4C55,
    "Delivery Bag": 0x803C4C56,
    "Hookshot": 0x803C4C57,
    "Skull Hammer": 0x803C4C58
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

toggle_bit_ownership = {
    "grappling_hook": 0x803C4C5C,
    "spoils_bag": 0x803C4C5D,
    "boomerang": 0x803C4C5E,
    "deku_leaf": 0x803C4C5F,
    "tingle_tuner": 0x803C4C5F,
    "iron_boots": 0x803C4C62,
    "magic_armor": 0x803C4C63,
    "bait_bag": 0x803C4C64,
    "bombs": 0x803C4C66,
    "delivery_bag": 0x803C4C6B,
    "hookshot": 0x803C4C6C,
    "skull_hammer": 0x803C4C6D,
    "power_bracelets": 0x803C4CBE
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
