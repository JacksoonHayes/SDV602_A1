player_inventory = set(['Torch'])

def display_inventory(inventory):
    if inventory == set([]):
        return "You have no items in your inventory."
    else:
        return "\n".join(f"{i + 1}. {item}" for i, item in enumerate(inventory))
    
def remove_item(item):
    player_inventory.remove(item)

def collect_item(item):
    player_inventory.add(item)

def inv_count():
    return (f"Inventory: {len(player_inventory)} / 7")

def show_inventory():
    return (f"Inventory: \n\n{display_inventory(player_inventory)}")
    
def has_item(item):
    return item in player_inventory

def clear_inventory():
    player_inventory.clear()
    player_inventory.add('Torch')