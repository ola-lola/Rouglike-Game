def create_board(width, height):
    board = []
    for x in range(height):
        row = []
        for y in range(width):
            if x < 1 or x == (height - 1) or y < 1 or y == (width - 1):
                row.append('#')
            else:
                row.append(' ')
        board.append(row)
    return board
    '''
    Creates a new game board based on input parameters.

    Args:
    int: The width of the board
    int: The height of the board

    Returns:
    list: Game board
    '''


def verify_move_is_possible(key_input, board, player):
    '''
    Modifies player coordinates if allowed (player cannot move through walls etc)

    Args:
    key_input: input string 'w', 's', 'a', 'd' etc.
    list: The game board
    dictionary: The player information containing the icon and coordinates

    Returns:
    Nothing
    '''
    pass


def put_player_on_board(board, player):
    '''
    Modifies the game board by placing the player icon at its coordinates.

    Args:
    list: The game board
    dictionary: The player information containing the icon and coordinates

    Returns:
    Nothing
    '''
    pass
