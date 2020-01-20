import items
import ui


# Define monsters attrbts/inventory function, needed as a dict with constant data when imported for operations in other modules
def monsters_overview():
    monsters = {
        "green": {
            "icon": ui.MONSTER_1,
            "damage": 10,
            "hps": 50,
            "experience": 25,
            "equipped": {"weapon": items.items_list()["weapons"]["stick"],
                         "armor": items.items_list()["armor"]["robe"]},
            "inventory": items.mob_inv(items.items_list(),items.greenItems)
            },
        "yellow": {
            "icon": ui.MONSTER_2,
            "damage": 10,
            "hps": 50,
            "experience": 25,
            "inventory": items.mob_inv(items.items_list(), items.yellowItems)
            },
        "red": {
            "icon": ui.MONSTER_3,
            "damage": 10,
            "hps": 50,
            "experience": 25,
            "inventory": items.items_list()
            },
        "boss": {
            "icon": ui.BOSS
        }
    }
    return monsters
