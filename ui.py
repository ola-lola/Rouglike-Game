import util


color_scheme = {0: ' ',     # BACKGROUND
                1: '#',     # WALL
                2: ' ',     # EXIT TO THE NEXT LEVEL
                '@': '@'}


def display_board(board):
    for line in board:
        for character in line:
            # print(color_scheme[character], end='')
            print(character, end='')
        print()


def calculate_max_column_width(column_name, column_data):
   
    max_column_width = 0

    if max_column_width <= len(column_name):
        max_column_width = len(column_name)

    if len(column_data) > 1:
        for item in column_data:
            if max_column_width < len(str(item)):
                max_column_width = len(str(item))
    else:
        if max_column_width < len(str(column_data)):
            max_column_width = len(str(column_data))

    return max_column_width



def print_table(player):
   
    max_lcol = calculate_max_column_width('Inventory', player)
    max_rcol = calculate_max_column_width('Inventory', player.values())

    print((max_lcol + 1) * "-" + (max_lcol + 2) * "-")
    print(f"{'~ WEAPON ~':^{max_lcol}} | {'count':^{max_lcol}}")
    print((max_lcol + 1) * "-" + (max_lcol + 2) * "-")

    for k, v in player['Inventory']['weapon items'].items():
        print(f"{k:^{max_lcol}} | {v:^{max_lcol}}")
    print((max_lcol + 1) * "-" + (max_lcol + 2) * "-")

    print(f"{'~ FOOD ~':^{max_lcol}} | {'count':^{max_lcol}}")
    print((max_lcol + 1) * "-" + (max_lcol + 2) * "-")


    for k, v in player['Inventory']['food items'].items():
        print(f"{k:^{max_lcol}} | {v:^{max_lcol}}")
    print((max_lcol + 1) * "-" + (max_lcol + 2) * "-")


    print(f"{'~ *** ~':^{max_lcol}} | {'count':^{max_lcol}}")
    print((max_lcol + 1) * "-" + (max_lcol + 2) * "-")


    for k, v in player['Inventory']['special items'].items():
        print(f"{k:^{max_lcol}} | {v:^{max_lcol}}")
    print((max_lcol + 1) * "-" + (max_lcol + 2) * "-")



def display_inventory(player, board):

    util.clear_screen()
    is_in_inventory = True
    while is_in_inventory:
        print_table(player)
        #print(player['Inventory'])
                                            

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
    
def display_mob(mob):
    pass

def display_boss(boss_array):
    for row in boss_array:
        for character in row:
            print(character, end='')
        print()

def display_fireball(character):
    pass

def display_bossRoom(room):
    pass
