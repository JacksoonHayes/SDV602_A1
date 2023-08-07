
player_inventory = set()

def collect_item(item):
    player_inventory.add(item)

def has_item(item):
    return item in player_inventory

def show_inventory():
    return (f"Inventory: \n\n{player_inventory}")
    
