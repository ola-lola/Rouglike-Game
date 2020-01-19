import tcod as libtcod
from input_handlers import handle_keys
from game_messages import MessageLog
import Entity
import util
import engine
import ui
import items
import render_functions
#from fov_functions import initialize_fov, recompute_fov
#from game_states import GameStates


PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50


BAR_WIDTH = 20
PANEL_HEIGHT = 7
PANEL_Y = SCREEN_HEIGHT - PANEL_HEIGHT
MESSAGE_X = BAR_WIDTH + 2
MESSAGE_WIDTH = SCREEN_WIDTH - BAR_WIDTH - 2
MESSAGE_HEIGHT = PANEL_HEIGHT - 1
MAP_WIDTH = 80
MAP_HEIGHT = 43


colors = {
    'dark_wall': libtcod.Color(0, 0, 100),
    'dark_ground': libtcod.Color(50, 50, 150)}



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
                "Inventory"     : {
                                }
    }
    #engine.add_to_inventory(player, ["club", "miecz", "miecz", "łuk", "proca"])
    #engine.add_to_inventory(player, ["chocolate", "bananas", "apples"])
    #items.equipWeapon(player, "club")

    return player
    '''
    Creates a 'player' dictionary for storing all player related information - i.e. player icon, player position.
    Fell free to extend this dictionary!

    Returns:
    dictionary
    '''


def main():
    # player = create_player()
    # level = 1
    # board = engine.create_board(level)

    libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
    libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'Hashed warrior stories', False)
    con = libtcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)


    #### CREATING NEW CONSOLE PANEL1 WITH HP
    panel = libtcod.console_new(SCREEN_WIDTH, PANEL_HEIGHT)


    player = create_player()
    #engine.damage_calculate(player)
    level = 1
    board = engine.create_board(level)

    #fov_map = initialize_fov(game_map)
    message_log = MessageLog(MESSAGE_X, MESSAGE_WIDTH, MESSAGE_HEIGHT)
    
    key = libtcod.Key()
    mouse = libtcod.Mouse()
    

    while not libtcod.console_is_window_closed():
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)

        ui.display_board(board, con)
        
        render_functions.render_all(con, panel, entities, player, game_map, fov_map, fov_recompute, message_log, SCREEN_WIDTH,
                  SCREEN_HEIGHT, BAR_WIDTH, PANEL_HEIGHT, PANEL_Y, mouse, colors)

        libtcod.console_set_default_foreground(con, libtcod.pink)
        libtcod.console_put_char(con, player['position']['x'], player['position']['y'], '@', libtcod.BKGND_NONE)
        libtcod.console_blit(con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 0)
        libtcod.console_flush()

        libtcod.console_put_char(con, player['position']['x'], player['position']['y'], ' ', libtcod.BKGND_NONE)

        action = handle_keys(key)

        move = action.get('move')
        go_to_inventory = action.get('go_to_inventory')
        exit = action.get('exit')
        fullscreen = action.get('fullscreen')

        if move:
            dx, dy = move
            engine.verify_move_is_possible(dx, dy, board, player, level)
            if engine.is_next_level(player["position"]["x"], player["position"]["y"], board, ">"):
                level += 1
                board = engine.create_board(level)
                player['position']['x'] = PLAYER_START_X
                player['position']['y'] = PLAYER_START_Y

        if go_to_inventory:
            ui.display_inventory(player, board, con)

        if exit:
            return True

        if fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())


if __name__ == '__main__':
    main()
