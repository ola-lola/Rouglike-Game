import tcod as libtcod
from input_handlers import handle_keys
import engine
import ui
import items

PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50

EXIT_SYMBOL = ">"


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
                                                    "key"       : 2
                                                    }
                                }
    }
    # engine.add_to_inventory(player, ["club", "miecz", "miecz", "łuk", "proca"])
    # engine.add_to_inventory(player, ["chocolate", "bananas", "apples"])

    return player
    '''
    Creates a 'player' dictionary for storing all player related information - i.e. player icon, player position.
    Fell free to extend this dictionary!

    Returns:
    dictionary
    '''


def create_new_game_window(screen_width, screen_height):
    # set window font
    libtcod.console_set_custom_font('arial12x12.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
    # create window with a given dimensions, name and False - not full screen
    libtcod.console_init_root(screen_width, screen_height, 'Hashed warrior stories', False)
    # initiate window and write it under a variable
    window = libtcod.console_new(screen_width, screen_height)
    return window


def main():
    game_window = create_new_game_window(SCREEN_WIDTH, SCREEN_HEIGHT)
    player = create_player()
    # engine.damage_calculate(player)
    level = 1
    board = engine.create_board(level)
    # variables to hold keyboard and mouse input
    key = libtcod.Key()
    mouse = libtcod.Mouse()

    while not libtcod.console_is_window_closed():
        # WAIT FOR INPUT
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)
        # DISPLAY BOARD + PLAYER ON BOARD
        ui.display_board(board, game_window)
        engine.put_player_on_board(game_window, SCREEN_WIDTH, SCREEN_HEIGHT, board, player)
        # GATHER KEY INPUT
        action = handle_keys(key)
        move = action.get('move')
        go_to_inventory = action.get('go_to_inventory')
        exit = action.get('exit')
        fullscreen = action.get('fullscreen')
        # HANDLE USER INPUT
        if move:
            dx, dy = move
            engine.verify_move_is_possible(dx, dy, board, player, level)
            if engine.is_next_level(player["position"]["x"], player["position"]["y"], board, EXIT_SYMBOL):
                level += 1
                board = engine.create_board(level)
                player['position']['x'] = PLAYER_START_X
                player['position']['y'] = PLAYER_START_Y
        if go_to_inventory:
            ui.display_inventory(player, game_window)
        if fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
        if exit:
            return True

if __name__ == '__main__':
    main()
