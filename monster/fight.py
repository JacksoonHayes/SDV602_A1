import inventory.inv as inventory
import cmd_parser.command_manager as cm
import status.health as health
import random

monster_health = 100

def fight():
    hit_chance = random.randint(1, 3)
    if hit_chance == 1:
        inventory.add_item('Key')
        return (f"You defeat the warrior in a duel.\nHe gives you a key.\n\n{cm.current_place()}")
    else:
        health.decrease_health(15)
        return (f"The warrior defeats you.\n\n{cm.current_place()}")
    
    
if __name__ == "__main__":
    while health.player_health > 0 or monster_health > 0:
        hit_chance = random.randint(1, 3)
        if hit_chance == 1:
            crit_chance = random.randint(1, 3)
            if crit_chance == 1:
                monster_health -= 50
                print(f"You hit the monster for 30 damage.\nMonster Health: {monster_health}")
            else:
                monster_health -= 25
                print(f"You hit the monster for 15 damage.\nMonster Health: {monster_health}")
        else:
            health.player_health -= 15
            print(f"The monster hit you for 5 damage.\nPlayer Health: {health.player_health}")