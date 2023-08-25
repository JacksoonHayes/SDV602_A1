"""
Inventory module.

This module provides functionality for managing and manipulating the player's inventory
in the game. This includes adding, removing, displaying items within the inventory.

Functions:
- display_inventory: Displays the player's inventory.
- remove_item: Removes a specified item from the player's inventory.
- collect_item: Adds a specified item to the player's inventory.
- inv_count: Gets the current count of items in the player's inventory.
- show_inventory: Displays all items in the player's inventory.
- has_item: Checks if a specified item is present in the player's inventory.
- clear_inventory: Clears all items from the player's inventory, and then adds back the 'Torch'.
"""


# A set to hold items in the player's inventory. Sets ensure unique items
# (no duplicates) and returns an unordered list.
player_inventory = set(['Torch'])


def display_inventory(inventory):
    """
    Displays the player's inventory.

    Args:
    - inventory (set): The inventory set containing items.

    Returns:
    - str: A representation of the items in the inventory.
    """
    # If the inventory is empty, inform the player.
    if not inventory:
        return "You have no items in your inventory."
    # Return an ordered string of items, using enumeration for indexing of
    # items.
    return "\n".join(f"{i + 1}. {item}" for i, item in enumerate(inventory))


def remove_item(item):
    """
    Removes a specified item from the player's inventory.

    Args:
    - item (str): The item to be removed.
    """
    player_inventory.remove(item)


def collect_item(item):
    """
    Adds a specified item to the player's inventory.

    Args:
    - item (str): The item to be added.
    """
    player_inventory.add(item)


def inv_count():
    """
    Gets the current count of items in the player's inventory.

    Returns:
    - str: A string showing the number of items and the maximum capacity.
    """
    return f"Inventory: {len(player_inventory)} / 7"


def show_inventory():
    """
    Displays all items in the player's inventory.

    Returns:
    - str: A representation of the items in the inventory.
    """
    return f"Inventory: \n\n{display_inventory(player_inventory)}"


def has_item(item):
    """
    Checks if a specified item is present in the player's inventory.

    Args:
    - item (str): The item to check.

    Returns:
    - bool: True if item is in inventory, else False.
    """
    return item in player_inventory


def clear_inventory():
    """
    Clears all items from the player's inventory, and then adds back the 'Torch'.
    """
    player_inventory.clear()
    player_inventory.add('Torch')


if __name__ == '__main__':
    print(show_inventory())
    collect_item('Sword')
    print(show_inventory())
    remove_item('Sword')
    print(show_inventory())
