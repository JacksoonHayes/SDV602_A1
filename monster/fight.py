import random

import inventory.inv as inventory
import cmd_parser.command_manager as cm
import status.health as health


# Function for the duel with the Knight. Knights health needs to be below
# 30 for the player to win. As its a duel the knight doesnt 'Die'
def duel(game_place):
    # Initialize health values for the player and the knight.
    knight_health = 100
    health_lost = 0

    # Continue the duel as long as the player has some health and knight's
    # health is above 30.
    while health.player_health > 0 and knight_health > 30:
        # Randomly determine if the player or the knight hits the opponent.
        hit_chance = random.randint(1, 2)

        if hit_chance == 1:
            # Determine if the player's hit is a critical hit.
            crit_chance = random.randint(1, 5)

            if crit_chance == 1:
                knight_health -= 30
                print(
                    f"You hit the knight for 30 damage.\nKnight Health: {knight_health}")
            else:
                knight_health -= 15
                print(
                    f"You hit the knight for 15 damage.\nknight Health: {knight_health}")
        else:
            # If knight hits, the player loses health.
            health.player_health -= 5
            health_lost += 5
            print(
                f"The knight hit you for 5 damage.\nPlayer Health: {health.player_health}")

    # Check the outcome of the duel.
    if knight_health <= 30:
        # Player collects a key if knight is defeated.
        inventory.collect_item('Key')
        return (f"{health.status()}\n\nYou defeat the Knight.\nHe gives you a key and leaves.\nYou have lost {health_lost} health from the duel.\n\n{cm.current_place()}")
    else:
        return (
            f"{health.status()}\n\nThe Knight defeats you.\n\n{cm.current_place()}")


def monster_fight(game_place):
    # Initialize health values for the player and the monster.
    monster_health = 100
    health_lost = 0

    # Continue the fight as long as the player has some health and monster's
    # health is above 30.
    while health.player_health > 0 and monster_health > 30:
        # Randomly determine if the player or the monster hits the opponent.
        hit_chance = random.randint(1, 2)

        if hit_chance == 1:
            # Determine if the player's hit is a critical hit.
            crit_chance = random.randint(1, 2)

            if crit_chance == 1:
                monster_health -= 30
                print(
                    f"You hit the Monster for 30 damage.\nMonster Health: {monster_health}")
            else:
                monster_health -= 15
                print(
                    f"You hit the Monster for 15 damage.\nMonster Health: {monster_health}")
        else:
            # If monster hits, the player loses health.
            health.player_health -= 5
            health_lost += 5
            print(
                f"The Monster hit you for 5 damage.\nPlayer Health: {health.player_health}")

    # Check the outcome of the monster fight.
    if monster_health <= 30:
        # Player collects a monster head if monster is defeated.
        inventory.collect_item('Monster Head')
        # Update the game story.
        cm.game_places['Lake']['Story'] = "You are at the Lake\n\nTo the East is a Town."
        return (f"{health.status()}\n\nYou defeat the Monster and collect its head.\nYou should return to the King.\nYou have lost {health_lost} health from the fight\n\n{cm.current_place()}")
    else:
        return (
            f"{health.status()}\n\nYou have lost to the monster.\n\n{cm.current_place()}")
