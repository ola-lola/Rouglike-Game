# KLUCZE ITEMS - zmienne globalne

# Define banned items for specific monster type
greenItems = [  "long_sword",
                "two-handed_sword",
                "light_sabre",
                "sword_of_doom",
                "leather_vest",
                "chain_mail",
                "plate_mail",
                "armor_of_doom"]

yellowItems = [ "light_sabre",
                "sword_of_doom",
                "plate_mail",
                "armor_of_doom"]


def items_list():
    items_list = {
        "food_items": {
                    "apple": {
                            "hp"    : 25,
                            "weight": 5
                            },
                    "healing_potion": {
                                        "hp"        : 100,
                                        "weight"    : 5
                                    },
                    "apple_pie": {
                                    "hp"    : 60,
                                    "weight": 10}
                    },
        "weapons": {
            "stick": {"damage": 1, "weight": 1},
            "club": {"damage": 3, "weight": 5},
            "short_sword": {"damage": 5, "weight": 15},
            "long_sword": {"damage": 10, "weight": 20},
            "two-handed_sword": {"damage": 20, "weight": 30},
            "light_sabre": {"damage": 25, "weight": 15},
            "sword_of_doom": {"damage": 35, "weight": 20}
        },
        "armor": {
            "robe": {"armor": 1, "weight": 1},
            "vest": {"armor": 3, "weight": 5},
            "leather_vest": {"armor": 5, "weight": 15},
            "chain_mail": {"armor": 10, "weight": 25},
            "plate_mail": {"armor": 25, "weight": 40},
            "armor_of_doom": {"armor": 40, "weight": 50}
        },
        "special items": {
            "gold coin" : {},
            "key"       : {}
        }
    }
    return items_list


# Define function for inventory of a given monster type, takes inv parameter as dict and banned parameter as list
def mob_inv(inv, banned):
    for key in inv.values():
        for item in banned:
            try:
                for nested_key in key:
                    if item in nested_key:
                        del key[nested_key]
            # Can't iterate over updated dict, need try-except block
            except RuntimeError:
                continue
    updated_inv = inv
    return updated_inv
