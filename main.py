import util
import engine
import ui

PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3

BOARD_WIDTH = 30
BOARD_HEIGHT = 20


def create_player(player):

    #1. Get a player's name from input
    name = input("Enter a name of player:  ")

    #2. Player's inventory with name, hps, position, available items etc.
    player = { "Name" : f'{name}' ,
                "Hps" : 100 ,
                "Experience" : 1,
                "Player position" : board[1][1] ,   ####<---- czy tak można zapisać pozycję?
                "Inventory" : { "food items" : { "chocolate" : 1, "bananas" : 3, "apples" : 2},
                                                "weapon items" : {"miecz" : 2, "łuk" : 1, "proca" : 4},
                                                "special items" : 0
                                            }
    }

    
    '''
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!

    Returns:
    dictionary
    '''


def main():
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
        if key == 'i':
            is_running = True
            ui.display_inventory(player)
            
        else:
            pass
        util.clear_screen()





if __name__ == '__main__':
    main()
