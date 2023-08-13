
import inventory.inv as inventory
import cmd_parser.command_manager as cm

player_health = 100

def show_health():
    return (f"Health: {player_health}")

def increase_health(amount):
    global player_health
    player_health += amount
    
def decrease_health(amount):
    global player_health
    player_health -= amount
    
def use_potion():
    if 'Potion' in inventory.player_inventory:
        inventory.player_inventory.remove('Potion')
        increase_health(30)
        return (f"You used a potion to increase your health by 20\n\n{cm.game_places[cm.game_state]['Story']}")