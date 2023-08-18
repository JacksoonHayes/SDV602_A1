import inventory.inv as inventory

player_health = 100

def status():
    return f"{show_health()}       {inventory.inv_count()}"

def show_health():
    return (f"Health: {player_health}")

def increase_health(amount):
    global player_health
    player_health += amount
    
def decrease_health(amount):
    global player_health
    player_health -= amount
