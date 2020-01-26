import tcod as libtcod
import pygame
from pygame import mixer
from input_handlers import handle_keys
import engine
import monsters
import ui
from player_def import create_player
import player_def
import introduction_screen


def main():
    pygame.mixer.init()
    engine.sound(engine._songs[0])
    level = 1
    game_window = ui.create_new_game_window(ui.SCREEN_WIDTH, ui.SCREEN_HEIGHT)
    player = create_player()
    board = engine.create_board(level)
    # PRINT INTRO MENU SCREEN (AND QUIT GAME IF USER CHOOSE SO)
    if introduction_screen.intro_menu_select(game_window) == -1:
        return 0
    # VARIABLES TO HOLD KEYBOARD AND MOUSE INPUT
    key = libtcod.Key()
    mouse = libtcod.Mouse()
    libtcod.console_clear(game_window)
    try:
        if level == 1:
            engine.sound(engine._songs[2])
        while not libtcod.console_is_window_closed():
            # WAIT FOR INPUT
            libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)
            # DISPLAY BOARD + PLAYER ON BOARD
            ui.display_board(board, game_window)
            ui.display_bar(player, game_window, board)
            engine.put_player_on_board(game_window, ui.SCREEN_WIDTH, ui.SCREEN_HEIGHT, board, player)
            # GATHER KEY INPUT
            action = handle_keys(key)
            move = action.get('move') # nazwy - do przeczytania np. should_move, is_exit
            go_to_inventory = action.get('go_to_inventory')
            fullscreen = action.get('fullscreen')
            exit = action.get('exit')
            # HANDLE USER INPUT
            if player["hps"] == 0:
                ui.final_screen(game_window, 'loose')
            if move:
                dx, dy = move
                player = engine.verify_move_is_possible(dx, dy, board, player, level, monsters.monsters_overview())
                footsteps_sound = pygame.mixer.Sound("walk.wav")
                footsteps_sound.set_volume(0.2)
                footsteps_sound.play(maxtime=1000)
                if engine.is_next_level(player["position"]["x"], player["position"]["y"], board, ui.EXIT_SYMBOL):
                    level += 1
                    board = engine.create_board(level)
                    player['position']['x'] = player_def.PLAYER_START_X
                    player['position']['y'] = player_def.PLAYER_START_Y
                    player['lvl'] += 1
                    player['experience'] += level*15
                    player['strenght'] += level*15
            if go_to_inventory:
                ui.display_inventory(player, game_window)
            if fullscreen:
                libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
            if exit:
                return True
    except IndexError:
        print('You went out of board bounds, please start the game again')



if __name__ == '__main__':
    main()
