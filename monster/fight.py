import inventory.inv as inventory
import cmd_parser.command_manager as cm
import status.health as health
import random

    
def duel(game_place):    
    knight_health = 100
    health_lost = 0
    while health.player_health > 0 and knight_health > 30:
        hit_chance = random.randint(1, 2)
        if hit_chance == 1:
            crit_chance = random.randint(1, 5)
            if crit_chance == 1:
                knight_health -= 30
                print(f"You hit the knight for 30 damage.\nKnight Health: {knight_health}")
            else:
                knight_health -= 15
                print(f"You hit the knight for 15 damage.\nknight Health: {knight_health}")
        else:
            health.player_health -= 5
            health_lost += 5
            print(f"The knight hit you for 5 damage.\nPlayer Health: {health.player_health}")
    if knight_health <= 30:
        inventory.collect_item('Key')
        return (f"{health.status()}\n\nYou defeat the Knight.\nHe gives you a key and leaves.\nYou have lost {health_lost} health from the duel.\n\n{cm.current_place()}")
    else:
        return (f"The Knight defeats you.\n\n{cm.current_place()}")

def monster_fight(game_place):    
    monster_health = 100
    health_lost = 0
    while health.player_health > 0 and monster_health > 30:
        hit_chance = random.randint(1, 2)
        if hit_chance == 1:
            crit_chance = random.randint(1, 2)
            if crit_chance == 1:
                monster_health -= 30
                print(f"You hit the Monster for 30 damage.\nMonster Health: {monster_health}")
            else:
                monster_health -= 15
                print(f"You hit the Monster for 15 damage.\nMonster Health: {monster_health}")
        else:
            health.player_health -= 5
            health_lost += 5
            print(f"The Monster hit you for 5 damage.\nPlayer Health: {health.player_health}")
    if monster_health <= 30:
        inventory.collect_item('Monster Head')
        cm.game_places['Lake']['Story'] = "You are at the Lake\n\nTo the East is a Town."
        return (f"{health.status()}\n\nYou defeat the Monster.\nYou have lost {health_lost} health from the fight\n\n{cm.current_place()}")
    else:
        return (f"You have lost to the monster.\n\n{cm.current_place()}")