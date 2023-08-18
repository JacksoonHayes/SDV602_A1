
player_inventory = set(['Torch'])

def display_inventory(inventory):
    if inventory == set([]):
        return "You have no items in your inventory."
    else:
        return "\n".join(f"{i + 1}. {item}" for i, item in enumerate(inventory))

def collect_item(item):
    player_inventory.add(item)

def inv_count():
    return (f"Inventory: {len(player_inventory)} / 5")

def show_inventory():
    return (f"Inventory: \n\n{display_inventory(player_inventory)}")
    
def has_item(item):
    return item in player_inventory
