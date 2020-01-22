import tcod as libtcod
import file_operations
import monsters
import random
import items
import ui


def monster_icons():
    icons = []
    for key in monsters.monsters_overview():
        for nest in monsters.monsters_overview()[key]:
            if nest == "icon":
                icons.append(monsters.monsters_overview()[key][nest])
    return icons


def create_board(level):
    filename = f"map{level}.txt"
    board = file_operations.import_board(filename)
    return board
    '''
    Creates a new game board based on input parameters.

    Args:
    int: level of the game

    Returns:
    list: Game board
    '''


def is_obstacle(x_coordinate, y_coordinate, board, border_symbols_list):
    if board[x_coordinate][y_coordinate] in border_symbols_list:
        return True
    else:
        return False


def is_next_level(x_coordinate, y_coordinate, board, border_exit_symbol):
    if board[x_coordinate][y_coordinate] in border_exit_symbol:
        return True
    else:
        return False


def is_newly_explored(x_coordinate, y_coordinate, board, player, gold_coin_symbol):
    if board[x_coordinate][y_coordinate] in gold_coin_symbol:
        return True
    else:
        return False


def verify_move_is_possible(move_x, move_y, board, player, level, mob_dict, mob=None):
    x = player['position']['x']
    y = player['position']['y']

    x_new = x + move_x
    y_new = y + move_y

    if not is_obstacle(x_new, y_new, board, [ui.WALL_SYMBOL, ui.TREE_SYMBOL, ui.WATER_SYMBOL]):
        player['position']['x'] = x_new
        player['position']['y'] = y_new
        board[x][y] = ' '

    if is_obstacle(x_new, y_new, board, [i for i in monster_icons()]):
        mob = board[x_new][y_new]
        fight_regular(player, mob_dict, mob) # dodac komunikat np. to nie jest zaimplem. w tej wersji

    if is_newly_explored(x_new, y_new, board, player, ui.BOARD_BACKGROUND_SYMBOL):
        player = add_to_inventory(player, ['gold coin'])
    # elif is_next_level(x_new, y_new, board, EXIT_SYMBOL):
    #     level += 1
        # player['position']['x'] = PLAYER_START_X
        # player['position']['y'] = PLAYER_START_Y
    return player
        
    '''
    Modifies player coordinates if allowed (player cannot move through walls etc)

    Args:
    key_input: input string 'w', 's', 'a', 'd' etc.
    list: The game board
    dictionary: The player information containing the icon and coordinates

    Returns:
    int: current level of the game
    '''


def put_player_on_board(window, window_width, window_height, board, player):
    # deprecated: 
    # x = player['position']['x']
    # y = player['position']['y']

    # board[x][y] = player['icon']

    libtcod.console_set_default_foreground(window, libtcod.pink)
    horizontal_offset = int((window_width/2)-(len(board)/2))
    libtcod.console_put_char(window, player['position']['x']+horizontal_offset, player['position']['y'], player['icon'], libtcod.BKGND_NONE)
    libtcod.console_blit(window, 0, 0, window_width, window_height, 0, 0, 0)
    libtcod.console_flush()
    libtcod.console_put_char(window, player['position']['x'], player['position']['y'], ' ', libtcod.BKGND_NONE)

    # TUTAJ IF-y dot food/item/mob

    '''
    Modifies the game board by placing the player icon at its coordinates.

    Args:
    list: The game board
    dictionary: The player information containing the icon and coordinates

    Returns:
    Nothing
    '''

def equipWeapon(player, weaponName):
    # Validate if item of same category already present, if present - unequip
    if weaponName not in player["inventory"]["weapons"]:
        return False
    wep_stats = items.items_list()["weapons"][weaponName]
    weapon_entry = {
        weaponName: wep_stats
    }
    player["equipped"]["weapons"][weaponName] = weapon_entry
    remove_from_inventory(player, weaponName)


def unequip(player, weaponName):
    if weaponName not in player["equipped"]["weapons"]:
        return False
    player["equipped"]["weapons"][weaponName].pop()
    add_to_inventory(player, weaponName)


def add_to_inventory_category(player, item, category):
    if item not in player["Inventory"][category].keys():
        player["Inventory"][category][item] = 1
    else:
        player["Inventory"][category][item] += 1


def add_to_inventory(player, added_items):
    all_available_items = items.items_list()
    # Doesn't work for single items, expects a list as param
    for item in added_items:
        for category in all_available_items.keys():
            if item in all_available_items[category]:
                add_to_inventory_category(player, item, category)
    return player

def remove_from_inventory(player, removed_items):
    for item in removed_items:
        for category in player["Inventory"].keys():
            if player["Inventory"][category][item] > 1:
                player["Inventory"][category][item] -= 1
            else:
                player["Inventory"][category].pop(item)
    return player


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


def damage_calculate(character):
    # Add null check for no weapons equipped
    try:
        weapontype = character["equipped"]["weapon"]["damage"]
        true_damage = character["strenght"] + weapontype + random.randint(1,10)
        return true_damage
        # Czy to key error?
    except KeyError:
        true_damage = character["strenght"] + random.randint(1,10)
        return true_damage

def health_calculate(character):
    try:
        health = character["hps"] + character["equipped"]["armor"]["armor"]
    except:
        health = character["hps"]
    return health

def find_mobStats(dictionary, mobName):
    for k,v in dictionary.items():
        for nested_keys in v.items():
            if mobName in nested_keys:
                return v  

def fight_regular(player, mob_dict, mob):
    player_hps = int(health_calculate(player))
    mob_hps = int(health_calculate(find_mobStats(mob_dict, mob)))
    while True:
        player_hps -= int(damage_calculate(find_mobStats(mob_dict, mob)))
        player["hps"] = player_hps
        if player_hps <= 0:
            player["hps"] = 0
            print(f'Your life remaining is: {player["hps"]}')
            print("FIGHT FINISHED\nYou died")
            break
        print(f"The monster attacks you for {int(damage_calculate(find_mobStats(mob_dict, mob)))} damage.\
                Your life remaining is: {player_hps}")
        mob_hps -= int(damage_calculate(player))
        if mob_hps <= 0:
            mob_hps = 0
            print(f"You attack the monster for {int(damage_calculate(player))} damage.\
                 Monster's health remaining: {mob_hps}")
            print("FIGHT FINISHED\nThe monster drops dead")
            break
        print(f"You attack the monster for {int(damage_calculate(player))} damage.\
                 Monster's health remaining: {mob_hps}")
        print()

        

def fight_boss():
    pass


def fireball(direction):
    pass

