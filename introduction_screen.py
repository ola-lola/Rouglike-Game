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
    horizontal_offset = int((ui.SCREEN_WIDTH/2)-(len(intro_board[0])/2))
    vertical_offset = int((ui.SCREEN_HEIGHT/2)-(len(intro_board)/2))

    key = libtcod.Key()
    mouse = libtcod.Mouse()

    introduction_menu = True
    libtcod.console_clear(window)
    while introduction_menu:

        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)

        for i, line in enumerate(intro_board):
            for j, char in enumerate(line):
                if char == '#':
                    libtcod.console_set_default_foreground(window, libtcod.light_chartreuse)
                else:
                    libtcod.console_set_default_foreground(window, libtcod.white)
                libtcod.console_put_char(window, j+horizontal_offset, i+vertical_offset, char, libtcod.BKGND_NONE)
                libtcod.console_blit(window, 0, 0, ui.SCREEN_WIDTH, ui.SCREEN_HEIGHT, 0, 0, 0)
                libtcod.console_flush()

        action = handle_keys(key)
        start_game = action.get('start_game')
        help = action.get('help')
        fullscreen = action.get('fullscreen')
        quit_menu = action.get('exit_menu')

        if start_game:
            libtcod.console_clear(window)
            return 0

        #display info/screen 'how to play'
        if help:
            libtcod.console_clear(window)
            how_to_play(window)

        if fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())

        if quit_menu:
            introduction_menu = False
            return -1


def create_character():
    symbols = ['@', '%', '$', '&']


def create_how_to_play_screen():
    filename = "how_to_play.txt"
    board = file_operations.import_board(filename)
    return board

def how_to_play(window):
    how_to_play_board = create_how_to_play_screen()
    horizontal_offset = int((ui.SCREEN_WIDTH/2)-(len(how_to_play_board[0])/2))
    vertical_offset = int((ui.SCREEN_HEIGHT/2)-(len(how_to_play_board)/2))

    key = libtcod.Key()
    mouse = libtcod.Mouse()

    how_to_play_descr = True
    libtcod.console_clear(window)
    while how_to_play_descr:

        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)

        for i, line in enumerate(how_to_play_board):
            for j, char in enumerate(line):
                if char in ["'", "`", "-", "\\", "/", "."]:
                    libtcod.console_set_default_foreground(window, libtcod.light_chartreuse)
                else:
                    libtcod.console_set_default_foreground(window, libtcod.white)
                libtcod.console_put_char(window, j+horizontal_offset, i+vertical_offset, char, libtcod.BKGND_NONE)
                libtcod.console_blit(window, 0, 0, ui.SCREEN_WIDTH, ui.SCREEN_HEIGHT, 0, 0, 0)
                libtcod.console_flush()

        action = handle_keys(key)
        back_to_menu = action.get('back')
        fullscreen = action.get('fullscreen')

        if fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())

        if back_to_menu:
            how_to_play_descr = False
            libtcod.console_clear(window)
            return -1




'''
def player_won_screen():
    filename = "youwon.txt"
    board = file_operations.import_board(filename)
    return board


def you_won(window):
    you_won_board = create_you_won_screen()
    horizontal_offset = int((ui.SCREEN_WIDTH/2)-(len(how_to_play_board[0])/2))
    vertical_offset = int((ui.SCREEN_HEIGHT/2)-(len(how_to_play_board)/2))

    key = libtcod.Key()
    mouse = libtcod.Mouse()

    how_to_play_descr = True
    libtcod.console_clear(window)
    while how_to_play_descr:

        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)

        for i, line in enumerate(how_to_play_board):
            for j, char in enumerate(line):
                if char in ["'", "`", "-", "\\", "/", "."]:
                    libtcod.console_set_default_foreground(window, libtcod.light_chartreuse)
                else:
                    libtcod.console_set_default_foreground(window, libtcod.white)
                libtcod.console_put_char(window, j+horizontal_offset, i+vertical_offset, char, libtcod.BKGND_NONE)
                libtcod.console_blit(window, 0, 0, ui.SCREEN_WIDTH, ui.SCREEN_HEIGHT, 0, 0, 0)
                libtcod.console_flush()

        action = handle_keys(key)
        back_to_menu = action.get('back')
        fullscreen = action.get('fullscreen')

        if fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())

        if back_to_menu:
            how_to_play_descr = False
            libtcod.console_clear(window)
            return -1
'''