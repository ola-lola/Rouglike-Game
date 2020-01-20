import items
import engine


PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3


def create_player():
    # 1. Get a player's name from input
    # name = input("Enter a name of player:  ")
    # 2. Player's inventory with name, hps, position, available items etc.
    player = {  "Name"          : 'Player',#f'{name}',
                "icon"          : PLAYER_ICON,
                "hps"           : 100,
                "strenght"      : 15,
                "experience"    : 1,
                "position"      : {
                                'x': PLAYER_START_X,
                                'y': PLAYER_START_Y,
                                },
                "equipped"      : {"weapon": {},
                                   "armor": items.items_list()["armor"]["robe"]},
                # NEED TO VALIDATE IF ADD TO INVENTORY FUNCTION IMPLEMENTS CATEGORIES FOR ITEMS
                "Inventory"     : {  "food items": {
                                                    "chocolate" : 1,
                                                    "apples"    : 2
                                                },
                                    "weapons": {
                                                    "miecz"     : 2,
                                                    "luk"       : 1,
                                                    "proca"     : 4
                                                    },
                                    "armor" : {},
                                    "special items": {
                                                    "gold coin" : 0,
                                                    "key"       : 2
                                                    }
                                }
    }
    # player = engine.add_to_inventory(player, ["gold coin", "gold_coin", "gold coin"])
    # engine.add_to_inventory(player, ["club", "miecz", "miecz", "łuk", "proca"])
    # engine.add_to_inventory(player, ["chocolate", "bananas", "apples"])

    return player
    '''
    Creates a 'player' dictionary for storing all player related information - i.e. player icon, player position.
    Fell free to extend this dictionary!

    Returns:
    dictionary
    '''