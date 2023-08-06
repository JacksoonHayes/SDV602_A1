import inventory.inv as inventory

player_health = 100

def show_status():
    return (f"Health: {player_health} \n\n{inventory.show_inventory()}")