

player_health = 100

def show_health():
    return (f"Health: {player_health}")

def increase_health(amount):
    global player_health
    player_health += amount
    
def decrease_health(amount):
    global player_health
    player_health -= amount