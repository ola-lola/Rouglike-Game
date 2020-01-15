import util


def display_board(board):
    for line in board:
        for character in line:
            print(character, end='')
        print()


def display_inventory(player, board):

    util.clear_screen()
    is_in_inventory = True
    while is_in_inventory:
        player_inventory = player['Inventory']
        print(player['Inventory'])
                                            ####<---- Jak odnieść się do defa gdzie jest umieszczony player?
                                            ####----- W ten sposób możemy się odnieść chyba tylko do zmiennej globalnej
        
    # Press 'i' to continue game on a board
        key = util.key_pressed()
        if key == 'i':
            is_running = True
            is_in_inventory = False
            display_board(board)
            
        else:
            pass
        util.clear_screen()


    '''
    Displays complete game board on the screen

    Returns:
    Nothing
    '''
