"""
Command parser/mananger module.

This module handles the games mechanics which involves navigating through different
locations and interacting with the environment with each location having its own
story and actions affecting the player's health and inventory.
"""


# Import modules to confine with the assessment scope.
import status.health as health
import inventory.inv as inventory
import cmd_parser.token as token
import monster.fight as fight


def move(game_place):
    """Move the player between different locations.

    Args:
        game_place (tuple): Contains the function to move and the new location.

    Returns:
        str: Current status of the player after the move.
    """
    global game_state

    # Decrease player health by 5 with each move
    health.decrease_health(5)
    game_state = game_place[1]  # Set the new game state based on the move

    # Return the current status of the player
    return current_status()


def use_potion(game_place):
    """Allow player to use a health potion.

    Args:
        game_place (tuple): Current game location and story.

    Returns:
        str: Player status and narrative after using a potion.
    """
    # Check if the player has a potion in their inventory
    if 'Potion' in inventory.player_inventory:
        # Use the potion and increase player's health by 50
        inventory.remove_item('Potion')
        health.increase_health(50)
        return (
            f"{health.status()}\n\nYou used a potion to increase your health by 50\n\n{current_place()}")
    return (f"{health.status()}\n\nYou have no potions to use\n\n{current_place()}")


# Function to change the story from the inital game start story.
def cave_story(game_place):
    """Narrative for entering a cave.

    Args:
        game_place (tuple): Contains the function to proceed and the associated location.

    Returns:
        str: Updated player status.
    """
    global game_state

    # Decrease player health by 5 with each move
    health.decrease_health(5)
    game_state = game_place[1]  # Set the new game state based on the move
    game_places['Cave']['Story'] = 'You are at the Cave.\n\nTo the South is a Town.\n\nDo you wish to enter the Cave?'
    return current_status()


def enter_cave(game_place):
    """Enter a cave if conditions are met.

    Args:
        game_place (tuple): Expected cave location and narrative.

    Returns:
        str: Resulting narrative after attempting to enter the cave.
    """
    result = ''
    # Player can enter the cave only if they have a torch
    if inventory.has_item('Torch'):
        result = move(game_place)
    else:
        # If the player does not have a torch, notify them (currently no way to
        # get a torch in the game, but spawn in with one on game start)
        result = f"{health.status()}\n\nYou need a torch to enter the cave.\n\n{current_place()}"
    return result


# Function to search the cave for items
def search_cave(game_place):
    # If the player already has a sword, there's nothing new to find
    if inventory.has_item('Sword'):
        return f"{health.status()}\n\nYou find nothing of interest.\n\n{current_place()}"

    # Otherwise, player discovers a sword
    inventory.collect_item('Sword')
    game_places[game_state]['Story'] = 'You are inside the cave\n\nDo you wish to leave?'
    return f"{health.status()}\n\nYou find a dull sword!\n\n{current_place()}"


# Check if the knight is in the forest
def is_knight_there(game_place):
    global game_places

    # If the player has a key, the knight is no longer in the forest
    if inventory.has_item('Key'):
        game_places['Forest']['Story'] = "You are in the Forest\n\nTo the West is a Town."
        return move((move, 'Forest'))
    return move(game_place)


# Function to handle player's interaction with the knight in the forest
def talk_to_knight(game_place):
    move((move, 'Knight'))
    # If the player has a sword, the knight challenges them to a duel
    if inventory.has_item('Sword'):
        return f"{health.status()}\n\nThe Knight requests a duel.\nYou can fight or leave?\n\n{current_place()}"
    return f"{health.status()}\n\nThe Knight is seeking a duel.\nReturn when you have a sword.\n\n{current_place()}"


# Function to manage the player's attempt to enter the castle
def enter_castle(game_place):
    result = ''
    # Player can only enter the castle if they have a key
    if inventory.has_item('Key'):
        result = move(game_place)
    else:
        # Notify player that they need a key and give a hint about its location
        result = f"{health.status()}\n\nA key is needed to enter the castle.\nPerhaps the man in the forest can help.\n\n{current_place()}"
    return result


# Function to handle the player's interaction with the king inside the castle
def talk_to_king(game_place):
    # If the player has defeated the monster, the king rewards them
    if inventory.has_item('Monster Head'):
        inventory.remove_item('Monster Head')
        inventory.collect_item('Cloak')
        return f"{health.status()}\n\nThe King thanks you for defeating the monster.\nYou receive a cloak for your efforts.\n\nYou have completed your adventure!"
    else:
        # If the player already has a shield or potion, the king won't talk
        if inventory.has_item('Shield') or inventory.has_item('Potion'):
            return f"{health.status()}\n\nThe King does not speak\n\n{current_place()}"
        else:
            # Otherwise, the king gives the player a quest and rewards them
            # with a shield and potion
            inventory.collect_item('Shield')
            inventory.collect_item('Potion')
            return f"{health.status()}\n\nThe King speaks of a bounty at the nearby lake.\nYou receive a shield and 1 health potion.\n\n{current_place()}"


# Function to manage the fight at the lake
def lake_fight(game_place):
    # Player can only challenge the monster if they have a shield
    if inventory.has_item('Shield'):
        return fight.monster_fight(game_place)
    else:
        # Notify player they need more equipment to challenge the monster
        return f"{health.status()}\n\nThe monster is too strong.\nReturn when you have a sword and shield.\n\nYou are at the Lake.\n\nTo the East is a Town."


"""
Defines the game places and their properties including what the player
can do at each place
Makes use of dictionaries and tuples to store the game places.
Dictionary keys and values are mutable.
Tuples are immutable and useful for storing data that will not change.
"""
game_state = 'Cave'
game_places = {'Town': {'Story': 'You are in a Town.\n\nTo the North is a Cave.\nTo the South is a Castle.\nTo the East is a Forest\nTo the West is a Lake.',
                        'North': (cave_story, 'Cave'),
                        'East': (is_knight_there, 'Forest'),
                        'South': (move, 'Castle'),
                        'West': (move, 'Lake'),
                        'Image': 'town.png',
                        'Potion': (use_potion, 'Town')
                        },
               'Cave': {'Story': 'You start your adventure on the way to explore a Cave.\n\nTo the South is a Town.\n\nDo you wish to enter the Cave?',
                        'South': (move, 'Town'),
                        'Enter': (enter_cave, 'InCave'),
                        'Image': 'cave.png',
                        'Potion': (use_potion, 'Cave')
                        },
               'InCave': {'Story': 'The cave is barren and dimly lit,\nbut it may be worth searching.\n\nSearch the cave?\n\nDo you wish to leave?',
                          'Leave': (cave_story, 'Cave'),
                          'Search': (search_cave, 'InCave'),
                          'Image': 'inCave.png',
                          'Potion': (use_potion, 'InCave')
                          },
               'Forest': {'Story': "You are greeted by a travelling Knight heading west\nTalk to the Knight?\n\nYou are in a Forest\n\nTo the West is a Town.",
                          'West': (move, 'Town'),
                          'Talk': (talk_to_knight, 'Knight'),
                          'Image': 'forest.png',
                          'Potion': (use_potion, 'Forest')
                          },
               'Knight': {'Story': 'You are in the Forest.\n\nTo the West is a Town.',
                          'West': (move, 'Town'),
                          'Leave': (move, 'Town'),
                          'Fight': (fight.duel, 'Knight'),
                          'Image': 'knight.png',
                          'Potion': (use_potion, 'Knight')
                          },
               'Castle': {'Story': 'You are at the Castle.\n\nTo the North is a Town.\n\nDo you wish to enter the Castle?',
                          'North': (move, 'Town'),
                          'Enter': (enter_castle, 'InCastle'),
                          'Image': 'castle.png',
                          'Potion': (use_potion, 'Castle')
                          },
               'InCastle': {'Story': 'The King is standing in front of you.\nTalk to the King?\n\nDo you wish to leave?',
                            'Leave': (move, 'Castle'),
                            'Talk': (talk_to_king, 'InCastle'),
                            'Image': 'castle.png',
                            'Potion': (use_potion, 'InCastle')
                            },
               'Lake': {'Story': 'A strong monster lurks near the waters edge.\nFight the monster?\n\nYou arrive at the Lake.\n\nTo the East is a Town.',
                        'East': (move, 'Town'),
                        'Fight': (lake_fight, 'Lake'),
                        'Image': 'lake.png',
                        'Potion': (use_potion, 'Lake')
                        },
               }


# Function to return the story of the current location
def current_place():
    """Gets the story at the game_state place

    Returns:
        string: the story at the current place
    """
    return f"{game_places[game_state]['Story']}"


# Same function as current_place() but with the players health and
# inventory status added.
def current_status():
    """Provide the player's health status along with the current location's story.

    Returns:
        str: Player's health and location story.
    """

    return f"{health.status()}\n\n{current_place()}"


# Main game function that takes user input and processes game mechanics
def game_play(user_input):
    """Main game loop that takes user input and processes game mechanics.

    Args:
        user_input (str): Direction or action input from the user.

    Returns:
        str: Narrative or result of the player's action.
    """

    while health.player_health > 0:
        story_result = ''
        valid_tokens = token.valid_list(user_input)
        if not valid_tokens:
            story_result = f"{health.status()}\n\nPlease enter a valid command.\n\n{current_place()}"
        else:
            for atoken in valid_tokens:
                game_place = game_places[game_state]
                the_place = atoken.capitalize()
                if the_place == "Talk" and game_state == "Forest" and inventory.has_item(
                        'Key'):
                    story_result = f"{health.status()}\n\nYou are in the Forest.\n\n,To the West is a Town."
                    continue
                if the_place == "Fight" and game_state == "Knight" and not inventory.has_item(
                        'Sword'):
                    story_result = talk_to_knight(game_place)
                    continue
                if the_place == "Fight" and game_state == "Knight" and inventory.has_item(
                        'Key'):
                    story_result = f"{health.status()}\n\nYou are in the Forest.\n\nTo the West is a Town."
                    continue
                if the_place == "Fight" and game_state == "Lake" and inventory.has_item(
                        'Monster Head'):
                    story_result = f"{health.status()}\n\nYou are at the Lake.\n\nTo the East is a Town."
                    continue
                if the_place in game_place:
                    place = game_place[the_place]
                    story_result = place[0](place)
                else:
                    story_result = f"{health.status()}\n\nYou can not do that from here.\n\n{current_place()}"
        return story_result
