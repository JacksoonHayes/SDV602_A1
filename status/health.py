"""
Status/Health Module.

This module provides functions for managing or displaying the player's health.

Functions:
- status: Provides a string representation of the player's health and inventory count.
- show_health: Displays the current health of the player.
- increase_health: Increases the player's health by a specified amount.
- decrease_health: Decreases the player's health by a specified amount.
"""

import inventory.inv as inventory

# Set player's health to 100.
player_health = 100

def status():
    """
    Provides the current status of the player. (health and inventory count)
    
    Returns:
    - str: A formatted string displaying player's health and number of items in the inventory.
    """
    return f"{show_health()}       {inventory.inv_count()}"

def show_health():
    """
    Dispalys the current health of the player.
    
    Returns:
    - str: A formatted string displaying player's health.
    """
    return f"Health: {player_health}"

def increase_health(amount):
    """
    Increases the player's health by the specified amount.
    
    Args:
    - amount (int): The amount by which to increase the player's health.
    """
    global player_health  # Using global keyword to modify the global variable.
    player_health += amount

def decrease_health(amount):
    """
    Decreases the player's health by the specified amount.
    
    Args:
    - amount (int): The amount by which to decrease the player's health.
    """
    global player_health  # Using global keyword to modify the global variable.
    player_health -= amount

if __name__ == '__main__':
    print(status())
    increase_health(20)
    print(status())
    decrease_health(10)
    print(status())
