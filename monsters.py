import items

# Define monsters attrbts/inventory function, needed as a dict with constant data when imported for operations in other modules
def monsters_overview():
    monsters = {
        "green": {
            "icon": "G",
            "damage": 10,
            "hps": 50,
            "experience": 25,
            "inventory": items.mob_inv(items.items_list(),items.greenItems)
            },
        "yellow": {
            "icon": "Y",
            "damage": 10,
            "hps": 50,
            "experience": 25,
            "inventory": items.mob_inv(items.items_list(), items.yellowItems)
            },
        "red": {
            "icon": "R",
            "damage": 10,
            "hps": 50,
            "experience": 25,
            "inventory": items.items_list()
            },
        "boss": {
            "icon": "B"
        }
    }
    return monsters

