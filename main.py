import tcod as libtcod
from input_handlers import handle_keys
import engine
import monsters
import ui
from player_def import create_player
import player_def
import introduction_screen


def main():
    game_window = ui.create_new_game_window(ui.SCREEN_WIDTH, ui.SCREEN_HEIGHT)
    player = create_player()
    level = 1
    board = engine.create_board(level)

    introduction_screen.intro_menu_select(game_window)


    # VARIABLES TO HOLD KEYBOARD AND MOUSE INPUT
    key = libtcod.Key()
    mouse = libtcod.Mouse()

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
        exit = action.get('exit')
        fullscreen = action.get('fullscreen')
        # HANDLE USER INPUT
        if player["hps"] == 0:
            ui.you_lost_screen(game_window)
        if move:
            dx, dy = move
            player = engine.verify_move_is_possible(dx, dy, board, player, level, monsters.monsters_overview())
            if engine.is_next_level(player["position"]["x"], player["position"]["y"], board, ui.EXIT_SYMBOL):
                level += 1
                board = engine.create_board(level)
                player['position']['x'] = player_def.PLAYER_START_X
                player['position']['y'] = player_def.PLAYER_START_Y
        if go_to_inventory:
            ui.display_inventory(player, game_window)
        if fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
        if exit:
            return True


if __name__ == '__main__':
    main()
