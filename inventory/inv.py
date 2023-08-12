
player_inventory = set(('Torch',))

def display_inventory(inventory):
    return "\n".join([f"{index}. {item}" for index, item in enumerate(sorted(inventory), 1)])

def collect_item(item):
    player_inventory.add(item)

def has_item(item):
    return item in player_inventory

def inv_count():
    return (f"Inventory: {len(player_inventory)} / 5")


item_list = display_inventory(player_inventory)

def show_inventory():
    return (f"Inventory: \n\n{item_list}")
    
