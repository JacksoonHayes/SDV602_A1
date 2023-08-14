
import inventory.inv as inventory
import cmd_parser.command_manager as cm

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
    
def use_potion(game_place):
    if 'Potion' in inventory.player_inventory:
        inventory.player_inventory.remove('Potion')
        increase_health(30)
        return (f"You used a potion to increase your health by 30\n\n{cm.current_place()}")
    else:
        return (f"You have no potions to use\n\n{cm.current_place()}")