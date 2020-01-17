import file_operations
import monsters


BOARD_BACKGROUND_SYMBOL = "." #0
WALL_SYMBOL = "#" #1
EXIT_SYMBOL = ">" #2
TREE_SYMBOL = "|"


def create_board(width, height, level=0):
    if level == 0:
        board = []
        for x in range(height):
            row = []
            for y in range(width):
                if x == (height - 2) and y == (width - 1):
                    row.append(EXIT_SYMBOL)
                elif x < 1 or x == (height - 1) or y < 1 or y == (width - 1):
                    row.append(WALL_SYMBOL)
                else:
                    row.append(BOARD_BACKGROUND_SYMBOL)
            board.append(row)
    else:
        filename = f"map{level}.txt"
        board = file_operations.import_board(filename)
    return board
    '''
    Creates a new game board based on input parameters.

    Args:
    int: The width of the board
    int: The height of the board

    Returns:
    list: Game board
    '''


def is_border(x_coordinate, y_coordinate, board, border_symbols_list):
    if board[x_coordinate][y_coordinate] in border_symbols_list:
        return True
    else:
        return False


def verify_move_is_possible(key_input, board, player):

    x = player['position']['x']
    y = player['position']['y']
    
    if key_input == 'w':
        x_new = x - 1
        y_new = y
    elif key_input == 's':
        x_new = x + 1
        y_new = y
    elif key_input == 'a':
        x_new = x
        y_new = y - 1
    elif key_input == 'd':
        x_new = x
        y_new = y + 1

    if not is_border(x_new, y_new, board, [WALL_SYMBOL, TREE_SYMBOL]):
        player['position']['x'] = x_new
        player['position']['y'] = y_new

        board[x][y] = ' '

    '''
    Modifies player coordinates if allowed (player cannot move through walls etc)

    Args:
    key_input: input string 'w', 's', 'a', 'd' etc.
    list: The game board
    dictionary: The player information containing the icon and coordinates

    Returns:
    Nothing
    '''


def put_player_on_board(board, player):

    x = player['position']['x']
    y = player['position']['y']

    board[x][y] = player['icon']

    # TUTAJ IF-y dot food/item/mob

    '''
    Modifies the game board by placing the player icon at its coordinates.

    Args:
    list: The game board
    dictionary: The player information containing the icon and coordinates

    Returns:
    Nothing
    '''


def add_to_inventory(player, added_items):
  
    for item in added_items:
        if item not in player["Inventory"].keys():
            player["Inventory"][item] = 1
        elif item in player["Inventory"]:
            player["Inventory"][item] += 1
    return player["Inventory"]


def remove_from_inventory(player, removed_items):

    for item in removed_items:
        if item in player["Inventory"].keys():
            if player["Inventory"][item] > 1:
                player["Inventory"][item] -= 1
            else:
                player["Inventory"].pop(item)
    return inventory

def random_mobPlace():
    pass

def random_mobMovement():
    pass

def generate_boss(width, height):
    boss = []
    for x in range(height):
        row = []
        for y in range(width):
            if x < 1 or x == (height - 1) or y < 1 or y == (width - 1):
                row.append(monsters.monsters_overview()["boss"]["icon"])
            else:
                row.append(" ")
        boss.append(row)
    return boss

def generate_bossRoom():
    pass

def fight_regular():
    pass

def fight_boss():
    pass

def fireball(direction):
    pass

