import tcod as libtcod
from input_handlers import handle_keys
import ui
import file_operations


def create_intro():
    filename = "introduction.txt"
    board = file_operations.import_board(filename)
    return board


def intro_menu_select(window):
    intro_board = create_intro()

    key = libtcod.Key()
    mouse = libtcod.Mouse()

    introduction_menu = True
    libtcod.console_clear(window)
    while introduction_menu:

        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)

        for i, line in enumerate(intro_board):
            for j, char in enumerate(line):
                libtcod.console_set_default_foreground(window, libtcod.amber)
                libtcod.console_put_char(window, j, i, char, libtcod.BKGND_NONE)
                libtcod.console_blit(window, 0, 0, ui.SCREEN_WIDTH, ui.SCREEN_HEIGHT, 0, 0, 0)
                libtcod.console_flush()

        # Press 'i' to continue game on a board
        action = handle_keys(key)
        start_game = action.get('start_game')
        help = action.get('help')
        quit_menu = action.get('exit_menu')

        if start_game:
            libtcod.console_clear(window)
            return 0

        #display info/screen 'how to play'
        elif help:
            pass

        elif quit_menu:
            introduction_menu = False
            return 0


def create_character():
    symbols = ['@', '%', '$', '&']
