import tcod as libtcod
from input_handlers import handle_keys
import items
import monsters
import file_operations

BOARD_BACKGROUND_SYMBOL = "."
WALL_SYMBOL = "#"
EXIT_SYMBOL = ">"
PORTAL_SYMBOL_AKA_WIN_SPOT = "*"
TREE_SYMBOL = "|"
WATER_SYMBOL = "o"

MONSTER_1 = "G"
MONSTER_2 = "Y"
MONSTER_3 = "R"
BOSS = "B"

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 53


def create_new_game_window(screen_width, screen_height):
    # set window font
    libtcod.console_set_custom_font('arial12x12.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
    # create window with a given dimensions, name and False - not full screen
    libtcod.console_init_root(screen_width, screen_height, 'Hashed warrior stories', False)
    # initiate window and write it under a variable
    window = libtcod.console_new(screen_width, screen_height)
    return window


def final_screen(window, loose_or_win):
    if loose_or_win == 'win':
        screen = file_operations.import_board("youwon.txt")
    else:
        screen = file_operations.import_board("youlost.txt")
    horizontal_offset = int((SCREEN_WIDTH/2)-(len(screen[0])/2))
    vertical_offset = int((SCREEN_HEIGHT/2)-(len(screen)/2))

    key = libtcod.Key()
    mouse = libtcod.Mouse()

    libtcod.console_clear(window)

    while not libtcod.console_is_window_closed():
        # WAIT FOR INPUT
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)

        action = handle_keys(key)
        fullscreen = action.get('fullscreen')
        exit = action.get('exit')

        for i, line in enumerate(screen):
            for j, char in enumerate(line):
                if loose_or_win == 'win':
                    if char == "M":
                        libtcod.console_set_default_foreground(window, libtcod.yellow)
                    elif char == "S":
                        libtcod.console_set_default_foreground(window, libtcod.blue)
                    elif char == "#":
                        libtcod.console_set_default_foreground(window, libtcod.light_chartreuse)
                    else:
                        libtcod.console_set_default_foreground(window, libtcod.white)
                else:
                    if char == "#":
                        libtcod.console_set_default_foreground(window, libtcod.red)
                    else:
                        libtcod.console_set_default_foreground(window, libtcod.white)
                libtcod.console_put_char(window, j+horizontal_offset, i+vertical_offset, char, libtcod.BKGND_NONE)
                libtcod.console_blit(window, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 0)
                libtcod.console_flush()

        if fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())

        if exit:
            return True


def display_board(board, window):
    horizontal_offset = int((SCREEN_WIDTH/2)-(len(board)/2))
    for i, line in enumerate(board):
        for j, char in enumerate(line):
            if char == WALL_SYMBOL:
                libtcod.console_set_default_foreground(window, libtcod.gray)
            elif char == EXIT_SYMBOL:
                libtcod.console_set_default_foreground(window, libtcod.yellow)
            elif char == TREE_SYMBOL:
                libtcod.console_set_default_foreground(window, libtcod.green)
            elif char == WATER_SYMBOL:
                libtcod.console_set_default_foreground(window, libtcod.blue)
            elif char == MONSTER_1:
                libtcod.console_set_default_foreground(window, libtcod.dark_green)
            elif char == MONSTER_2:
                libtcod.console_set_default_foreground(window, libtcod.dark_amber)
            elif char == MONSTER_3:
                libtcod.console_set_default_foreground(window, libtcod.dark_red)
            else:
                libtcod.console_set_default_foreground(window, libtcod.light_azure)
            libtcod.console_put_char(window, (i+horizontal_offset), j, char, libtcod.BKGND_NONE)


def calculate_max_column_width(column_names, column_data):
    max_column_width = 0
    if len(column_names) == 1:
        if max_column_width <= len(column_names):
            max_column_width = len(column_names)
    else:
        for name in column_names:
            if max_column_width <= len(column_names):
                max_column_width = len(column_names)
    if len(column_data) > 1:
        for item in column_data:
            if max_column_width < len(str(item)):
                max_column_width = len(str(item))
    else:
        if max_column_width < len(str(column_data)):
            max_column_width = len(str(column_data))
    return max_column_width


def print_table(player):
    # max_lcol TO BE UPDATED - PROBABLY WRONG
    max_lcol = calculate_max_column_width(player['Inventory'].keys(), player['Inventory'].values())

    if player['Inventory'] == {}:
        string_to_print = "Player's inventory is empty"
    else:
        separator = ((max_lcol + 1) * "-" + (max_lcol + 2) * "-") + "\n"
        string_to_print = separator

        for category in player['Inventory']:
            string_to_print += (f"{category.upper():^{max_lcol}} | {'COUNT':^{max_lcol}}") + "\n" \
                + separator
            for k, v in player['Inventory'][category].items():
                string_to_print += (f"{k:^{max_lcol}} | {v:^{max_lcol}}") + "\n"
            string_to_print += separator

    return string_to_print


def display_inventory(player, window):
    string_inventory = print_table(player)
    inventory_to_display = string_inventory.split("\n")
    horizontal_offset = int((SCREEN_WIDTH/2)-(len(inventory_to_display[0])/2))
    vertical_offset = int((SCREEN_HEIGHT/2)-(len(inventory_to_display)/2))

    key = libtcod.Key()
    mouse = libtcod.Mouse()

    is_in_inventory = True
    libtcod.console_clear(window)
    while is_in_inventory:

        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)

        for i, line in enumerate(inventory_to_display):
            for j, char in enumerate(line):
                if char == '-' or char == '|':
                    libtcod.console_set_default_foreground(window, libtcod.light_chartreuse)
                else:
                    libtcod.console_set_default_foreground(window, libtcod.white)
                libtcod.console_put_char(window, j+horizontal_offset, i+vertical_offset, char, libtcod.BKGND_NONE)
                libtcod.console_blit(window, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 0)
                libtcod.console_flush()

        # Press 'i' to continue game on a board
        action = handle_keys(key)
        fullscreen = action.get('fullscreen')
        go_out_from_inventory = action.get('go_to_inventory')

        if fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())

        if go_out_from_inventory:
            libtcod.console_clear(window)
            is_in_inventory = False
    '''
    Displays complete game board on the screen

    Returns:
    Nothing
    '''


def print_bar(player): 
    max_lcol = calculate_max_column_width('Name', [])

    string_to_print_bar = (SCREEN_WIDTH * "-") + "\n"

    string_to_print_bar += (f"{'NAME':^{max_lcol}}:{str(player['Name']):^{max_lcol}} | ")
    string_to_print_bar += (f"{'RACE':^{max_lcol}}:{str(player['race']):^{max_lcol}} | ")
    string_to_print_bar += (f"{'XP':^{max_lcol}}:{str(player['experience']):^{max_lcol}} | ")
    string_to_print_bar += (f"{'LVL':^{max_lcol}}:{str(player['lvl']):^{max_lcol}} | ")
    string_to_print_bar += (f"{'STR':^{max_lcol}}:{str(player['strenght']):^{max_lcol}} | ")
    string_to_print_bar += (f"{'HPS':^{max_lcol}}:{str(player['hps']):^{max_lcol}} | ")

    #for k, v in player.items():
        #string_to_print_bar += (f"{k:^{max_lcol}}:{str(v):^{max_lcol}} | ")
    string_to_print_bar += "\n" + (SCREEN_WIDTH * "-") + "\n"
    

    return string_to_print_bar

def display_bar(player, window, board):

    string_bar = print_bar(player)
    bar_to_display = string_bar.split("\n")
   
    horizontal_offset = 0
    vertical_offset = int(SCREEN_HEIGHT - 3)

    for i, line in enumerate(bar_to_display):
        for j, char in enumerate(line):
            if char == "-":
                libtcod.console_set_default_foreground(window, libtcod.dark_green)
            elif char == "|":
                libtcod.console_set_default_foreground(window, libtcod.dark_green)
     
            else:
                libtcod.console_set_default_foreground(window, libtcod.white)
            libtcod.console_put_char(window, j+horizontal_offset, i+vertical_offset, char, libtcod.BKGND_NONE)




def display_mob(mob):
    pass


def display_boss(boss_array):
    for row in boss_array:
        for character in row:
            print(character, end='')
        print()


def display_fireball(character):
    pass


def display_bossRoom(room):
    pass
