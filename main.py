import util
import engine
import ui

PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3

BOARD_WIDTH = 59
BOARD_HEIGHT = 59


def create_player():

    #1. Get a player's name from input
    name = input("Enter a name of player:  ")

    #2. Player's inventory with name, hps, position, available items etc.
    player = {  "Name" : f'{name}' ,
                "icon": PLAYER_ICON,
                "Hps" : 100 ,
                "Experience" : 1,
                "position" : {
                    'x': PLAYER_START_X,
                    'y': PLAYER_START_Y,
                },
                "Inventory" : { "food items" : { "chocolate" : 1, "bananas" : 3, "apples" : 2},
                                "weapon items" : {"miecz" : 2, "łuk" : 1, "proca" : 4},
                                "special items" : {"key" : 2}
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
    movement_keys = ['w','s','a','d']
    player = create_player()
    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)

    util.clear_screen()
    is_running = True
    while is_running:
        engine.put_player_on_board(board, player)
        ui.display_board(board)

        key = util.key_pressed()
        if key == 'q':
            is_running = False
    # Press 'i' to check your inventory status
        elif key == 'i':
            is_running = True
            ui.display_inventory(player, board)            
        elif key in movement_keys:
            engine.verify_move_is_possible(key.lower(), board, player)
            engine.put_player_on_board(board, player)
        else:
            pass
        util.clear_screen()





if __name__ == '__main__':
    main()
