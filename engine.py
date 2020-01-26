import tcod as libtcod
import pygame
import file_operations
import monsters
import random
import items
import ui
import player_def
from input_handlers import handle_keys

_songs = ['menu.wav', 'engame.wav', 'bossfight.wav', 'fight.wav', 'dg1.ogg', 'dg2.mp3']

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
        fight_regular(0, player, mob_dict, mob) # dodac komunikat np. to nie jest zaimplem. w tej wersji

    if is_newly_explored(x_new, y_new, board, player, ui.BOARD_BACKGROUND_SYMBOL):
        player = add_to_inventory(player, ['gold coin'])
        player['hps'] += 1

    if is_obstacle(x_new, y_new, board, ui.PORTAL_SYMBOL_AKA_WIN_SPOT):
        ui.final_screen(0, 'win')

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
    except KeyError:
        true_damage = character["strenght"] + random.randint(1, 10)
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


def fight_regular(window, player, mob_dict, mob):
    player_hps = int(health_calculate(player))
    mob_hps = int(health_calculate(find_mobStats(mob_dict, mob)))

    libtcod.console_clear(window)
    key = libtcod.Key()
    mouse = libtcod.Mouse()

    total_string_to_print = ''

    fight_finished = False
    are_fighting = True

    while not fight_finished:
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)
        while are_fighting:
            player_hps -= int(damage_calculate(find_mobStats(mob_dict, mob)))
            player["hps"] = player_hps
            if player_hps <= 0:
                player["hps"] = 0
                string_to_print = f'Your life remaining is: {player["hps"]}\n\n' \
                    + 'FIGHT FINISHED\n\nYou died\n\n'
                total_string_to_print += string_to_print
                sound(_songs[4])
                are_fighting = False
                break
            else:
                string_to_print = f'The monster attacks you for {int(damage_calculate(find_mobStats(mob_dict, mob)))} damage.\n'\
                        + f'Your life remaining is: {player_hps}\n\n'
                total_string_to_print += string_to_print
            mob_hps -= int(damage_calculate(player))
            if mob_hps <= 0:
                mob_hps = 0
                string_to_print = f'You attack the monster for {int(damage_calculate(player))} damage.\n'\
                    + f'Monster\'s health remaining: {mob_hps}\n\n' \
                    + '\n\nFIGHT FINISHED\nThe monster drops dead\n\n'
                total_string_to_print += string_to_print
                loot_dead = monster_loot(find_mobStats(mob_dict, mob))
                #TUTAJ NA LOOTWANIE
                add_to_inventory(player, loot_dead)
                total_string_to_print += '\n\n You collect the following items\n from him to your backpack:\n'
                if loot_dead == {}:
                    total_string_to_print += ' * ' + 'No items to collect, sorry\n'
                else:
                    for i in loot_dead:
                        total_string_to_print += ' * ' + str(i) + '\n'
                are_fighting = False
                break
            else:
                string_to_print = f'You attack the monster for {int(damage_calculate(player))} damage.\n'\
                    + f'Monster\'s health remaining: {mob_hps}\n\n'
            total_string_to_print += string_to_print

        total_string_to_print_list = total_string_to_print.split('\n')
        horizontal_offset = int((ui.SCREEN_WIDTH/2)-(len(total_string_to_print_list[0])/2))
        vertical_offset = int((ui.SCREEN_HEIGHT/2)-(len(total_string_to_print_list)/2))
        last_rows = -(ui.SCREEN_HEIGHT)
        total_string_to_print_list = total_string_to_print_list[last_rows:]

        for i, line in enumerate(total_string_to_print_list):
            for j, char in enumerate(line):
                if 'drops dead' in line:
                    libtcod.console_set_default_foreground(window, libtcod.light_chartreuse)
                elif 'You died' in line:
                    libtcod.console_set_default_foreground(window, libtcod.lighter_red)
                elif 'The monster' in line or 'Your' in line:
                    libtcod.console_set_default_foreground(window, libtcod.lightest_blue)
                else:
                    libtcod.console_set_default_foreground(window, libtcod.white)
    
                libtcod.console_put_char(window, j+horizontal_offset, i+vertical_offset, char, libtcod.BKGND_NONE)
                libtcod.console_blit(window, 0, 0, ui.SCREEN_WIDTH, ui.SCREEN_HEIGHT, 0, 0, 0)
                libtcod.console_flush()

        # Press 'f' to continue game on a board
        action = handle_keys(key)
        fight_finished = action.get('fight_end')

        if fight_finished:
            libtcod.console_clear(window)
            fight_finished = True


def loot_randomItem(monster_dict, category, range_num, destination_dict):
    for i in range(range_num):
        random_pair = key, val = random.choice(list(monster_dict["inventory"][category].items()))
        x, y = random_pair     
        destination_dict[x] = y
    return destination_dict

def add_lootToInv(mobName,player):
    for k in monster_loot(find_mobStats(monsters.monsters_overview(), mobName)).keys():
        player["Inventory"] = k
    return player



def monster_loot(monster_dict):
    #random_consumbale = monster["inventory"]["food_items"]
    loot_corpse = {}
    try: 
        loot_randomItem(monster_dict, "food_items", 1, loot_corpse)
        loot_randomItem(monster_dict, "weapons", 2, loot_corpse)
        loot_randomItem(monster_dict, "armor", 2, loot_corpse)
    except:
        print("Not enough items to add to random monster inventory for looting")
    return loot_corpse


def choice_loot(monster_loot):
    """ Create a function for providing input for F1-F4 keys that correspond
        to the monster_loot dictionary items"""
    pass

def sound(file):
    pygame.init()
    pygame.mixer_music.load(file)
    pygame.mixer_music.play(-1)

