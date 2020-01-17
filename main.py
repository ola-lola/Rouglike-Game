import util
import engine
import ui

PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3


def create_player():
    # 1. Get a player's name from input
    name = input("Enter a name of player:  ")
    # 2. Player's inventory with name, hps, position, available items etc.
    player = {  "Name"          : f'{name}',
                "icon"          : PLAYER_ICON,
                "Hps"           : 100,
                "Experience"    : 1,
                "position"      : {
                                'x': PLAYER_START_X,
                                'y': PLAYER_START_Y,
                                },
                "Inventory"     : { "food items": {
                                                    "chocolate" : 1,
                                                    "bananas"   : 3,
                                                    "apples"    : 2
                                                },
                                    "weapon items": {
                                                    "miecz"     : 2,
                                                    "łuk"       : 1,
                                                    "proca"     : 4
                                                    },
                                    "special items": {
                                                    "key"       : 2
                                                    }
                                }
    }
    return player

    
    '''
    Creates a 'player' dictionary for storing all player related information - i.e. player icon, player position.
    Fell free to extend this dictionary!

    Returns:
    dictionary
    '''


def main():
    movement_keys = ['w', 's', 'a', 'd']
    player = create_player()
    level = 1
    board = engine.create_board(LEVEL)

    util.clear_screen()
    is_running = True
    while is_running:
        engine.put_player_on_board(board, player)
        ui.display_board(board)

        key = util.key_pressed()
        # MOVE THE PLAYER
        if key in movement_keys:
            engine.verify_move_is_possible(key.lower(), board, player, level)
            if engine.is_next_level(player["position"]["x"], player["position"]["y"], board, ">"):
                level += 1
                board = engine.create_board(level)
                player['position']['x'] = PLAYER_START_X
                player['position']['y'] = PLAYER_START_Y
            engine.put_player_on_board(board, player)
        # CHECK INVENTORY
        elif key == 'i':
            is_running = True
            ui.display_inventory(player, board)
        # QUIT GAME
        elif key == 'q':
            is_running = False
        else:
            pass
        util.clear_screen()


if __name__ == '__main__':
    main()
