import tcod as libtcod
import util


BOARD_BACKGROUND_SYMBOL = "."
WALL_SYMBOL = "#"
EXIT_SYMBOL = ">"
TREE_SYMBOL = "|"
WATER_SYMBOL = "o"


def display_board(board, window):
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
            else:
                libtcod.console_set_default_foreground(window, libtcod.light_azure)
            libtcod.console_put_char(window, i, j, char, libtcod.BKGND_NONE)


def calculate_max_column_width(column_name, column_data):
    max_column_width = 0
    if max_column_width <= len(column_name):
        max_column_width = len(column_name)
    if len(column_data) > 1:
        for item in column_data:
            if max_column_width < len(str(item)):
                max_column_width = len(str(item))
    else:
        if max_column_width < len(str(column_data)):
            max_column_width = len(str(column_data))
    return max_column_width


def print_table(player): # <-- TO BE REFACTORED - REPEATING CODE BLOCKS
    max_lcol = calculate_max_column_width('Inventory', player)
    # max_rcol = calculate_max_column_width('Inventory', player.values()) <-- NEVER USED

    print((max_lcol + 1) * "-" + (max_lcol + 2) * "-")
    print(f"{'~ WEAPON ~':^{max_lcol}} | {'count':^{max_lcol}}")
    print((max_lcol + 1) * "-" + (max_lcol + 2) * "-")

    for k, v in player['Inventory']['weapon items'].items():
        print(f"{k:^{max_lcol}} | {v:^{max_lcol}}")
    print((max_lcol + 1) * "-" + (max_lcol + 2) * "-")

    print(f"{'~ FOOD ~':^{max_lcol}} | {'count':^{max_lcol}}")
    print((max_lcol + 1) * "-" + (max_lcol + 2) * "-")

    for k, v in player['Inventory']['food items'].items():
        print(f"{k:^{max_lcol}} | {v:^{max_lcol}}")
    print((max_lcol + 1) * "-" + (max_lcol + 2) * "-")

    print(f"{'~ *** ~':^{max_lcol}} | {'count':^{max_lcol}}")
    print((max_lcol + 1) * "-" + (max_lcol + 2) * "-")

    for k, v in player['Inventory']['special items'].items():
        print(f"{k:^{max_lcol}} | {v:^{max_lcol}}")
    print((max_lcol + 1) * "-" + (max_lcol + 2) * "-")


def display_inventory(player, board, window):
    util.clear_screen()
    is_in_inventory = True
    while is_in_inventory:
        print_table(player)
        # Press 'i' to continue game on a board
        key = util.key_pressed()
        if key == 'i':
            is_in_inventory = False
            display_board(board, window)
        else:
            pass
        util.clear_screen()
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
