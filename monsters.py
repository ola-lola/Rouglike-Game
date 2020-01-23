import items
import ui

# Define monsters attrbts/inventory function, needed as a dict with constant data when imported for operations in other modules
def monsters_overview():
    monsters = {
        "green": {
            "icon": ui.MONSTER_1,
            "hps": 50,
            "strenght": 10,
            "experience": 25,
            "equipped": {"weapon": items.items_list()["weapons"]["stick"],
                         "armor": items.items_list()["armor"]["robe"]},
            "inventory": items.mob_inv(items.items_list(),items.greenItems)
            },
        "yellow": {
            "icon": ui.MONSTER_2,
            "strenght": 40,
            "hps": 150,
            "experience": 50,
            "inventory": items.mob_inv(items.items_list(), items.yellowItems)
            },
        "red": {
            "icon": ui.MONSTER_3,
            "strenght": 80,
            "hps": 520,
            "experience": 75,
            "inventory": items.items_list()
            },
        "boss": {
            "icon": ui.BOSS,
            "strenght": 100,
            "hps": 750,
            "experience": 100,
        }
    }
    return monsters
