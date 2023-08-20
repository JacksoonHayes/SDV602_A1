# A set to hold items in the player's inventory. Sets ensure unique items (no duplicates) and returns unordered.
player_inventory = set(['Torch'])

def display_inventory(inventory):
    # If the inventory is empty, inform the player.
    if inventory == set([]):
        return "You have no items in your inventory."
    # Return a ordered string of items, using enumeration for indexing.
    return "\n".join(f"{i + 1}. {item}" for i, item in enumerate(inventory))

def remove_item(item):
    # Removes the specified item from the player's inventory.
    player_inventory.remove(item)

def collect_item(item):
    # Adds the specified item to the player's inventory.
    player_inventory.add(item)

def inv_count():
    # Shows the current number of items and the maximum capacity.
    return (f"Inventory: {len(player_inventory)} / 7")

def show_inventory():
    # Displays all items in the player's inventory.
    return (f"Inventory: \n\n{display_inventory(player_inventory)}")

def has_item(item):
    # Checks if a specified item is present in the player's inventory.
    return item in player_inventory

def clear_inventory():
    # Clears all items from the player's inventory and re-adds the 'Torch' for story purposes.
    player_inventory.clear()
    player_inventory.add('Torch')
