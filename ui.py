import tcod as libtcod
from input_handlers import handle_keys
import items


BOARD_BACKGROUND_SYMBOL = "."
WALL_SYMBOL = "#"
EXIT_SYMBOL = ">"
TREE_SYMBOL = "|"
WATER_SYMBOL = "o"

MONSTER_1 = "G"
MONSTER_2 = "Y"
MONSTER_3 = "R"

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50


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
