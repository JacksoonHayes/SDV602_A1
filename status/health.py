import inventory.inv as inventory

# Set player's health to 100.
player_health = 100

def status():
    # Returns a string with current status. (health and inventory count)
    return f"{show_health()}       {inventory.inv_count()}"

def show_health():
    # Returns the player's current health as a string.
    return (f"Health: {player_health}")

def increase_health(amount):
    # Increases the player's health by the given amount.
    global player_health  # Using global keyword to modify the global variable.
    player_health += amount

def decrease_health(amount):
    # Decreases the player's health by the given amount.
    global player_health  # Using global keyword to modify the global variable.
    player_health -= amount
