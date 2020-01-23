import tcod as libtcod


def handle_keys(key):
    # Movement keys
    if key.vk == libtcod.KEY_UP:
        return {'move': (0, -1)}
    elif key.vk == libtcod.KEY_DOWN:
        return {'move': (0, 1)}
    elif key.vk == libtcod.KEY_LEFT:
        return {'move': (-1, 0)}
    elif key.vk == libtcod.KEY_RIGHT:
        return {'move': (1, 0)}

    elif key.vk == libtcod.KEY_CHAR:
        if key.c == ord('i'):
            return {'go_to_inventory': True}
        if key.c == ord('p'):
            return {'see_player_statistics': True}
        if key.c == ord('f'):
            return {'fight_end': True}

    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # Alt+Enter: toggle full screen
        return {'fullscreen': True}

    if key.vk == libtcod.KEY_1:
        return {'start_game': True}
    elif key.vk == libtcod.KEY_2:
        return {'help': True}
    elif key.vk == libtcod.KEY_3:
        return {'exit_menu': True}
    elif key.vk == libtcod.KEY_4:
        return {'back': True}

    elif key.vk == libtcod.KEY_ESCAPE:
        # Exit the game
        return {'exit': True}

    # No key was pressed
    return {}
