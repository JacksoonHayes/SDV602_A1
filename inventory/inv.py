
player_inventory = set(["1, 3", "sword", "shield", "potion"])
display_inventory = str(player_inventory)

# set to store the thing, tuple with item appended into to display in gui ((1., Sword)(2., Shield)(3., APPEND HERE))

def collect_item(item):
    player_inventory.add(item)

def has_item(item):
    return item in player_inventory

def inv_count():
    return (f"Inventory: {len(player_inventory)} / 5")

def show_inventory():
    return (f"Inventory: \n\n{display_inventory}")
    
