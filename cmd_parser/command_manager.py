import status.health as health
import inventory.inv as inventory
import cmd_parser.token as token


def move(game_place):
    global game_state
    
    game_state = game_place[1]
    return current_status()


def enter_cave(game_place):
    result = ''
    if inventory.has_item('Torch'):
        result = move(game_place)
    else:
        result = f"You need a torch to enter the cave.\n\n{current_place()}"
    return result

def search_cave(game_place):
    if inventory.has_item('Sword'):
        return f"You find nothing of interest.\n\n{current_place()}"
    else:
        inventory.collect_item('Sword')
        game_places[game_state]['Story'] = 'You are inside the cave\n\nDo you wish to leave?'
        return f"You find a dull sword!\n\n{current_place()}"
    
def enter_castle(game_place):
    result = ''
    if inventory.has_item('Key'):
        result = move(game_place)
    else:
        result = f"A key is needed to enter the castle.\nPerhaps the man in the forest can help.\n\n{current_place()}"
    return result

def talk_to_king(game_place):
    if inventory.has_item('Shield') or inventory.has_item('Potion'):
        return f"The King does not speak\n\n{current_place()}"
    else:
        inventory.collect_item('Shield')
        inventory.collect_item('Potion')
        game_places[game_state]['Story'] = 'You are inside the castle\n\nDo you wish to leave?'
        return f"The King speaks of a bounty at the nearby lake,\nyou recieve a shield and potion.\n\n{current_place()}"


def is_knight_there(game_place):
    global game_places
    
    if inventory.has_item('Key'):
        game_places['Forest']['Story'] = "You are in a Forest\n\nTo the West is a Town."
        return move((move, 'Forest'))
    else:
        return move(game_place)
    
def talk_to_knight(game_place):
    if inventory.has_item('Sword'):
        return f"The Knight does not speak\n\n{current_place()}"
        
    else:
        game_places['Knight']['Story'] = 'Return when you have a sword'
        return move((move, 'Knight'))
    
    
def use_potion():
    if 'Potion' in inventory.player_inventory:
        inventory.remove_item('Potion')
        health.increase_health(40)
        return (f"You used a potion to increase your health by 30\n\n{current_place()}")
    else:
        return (f"You have no potions to use\n\n{current_place()}")
        
        
# Brief comment about how the following lines work
game_state = 'Town'
game_places = {'Town': {'Story': 'You are in a Town.\n\nTo the North is a Cave.\nTo the South is a Castle.\nTo the East is a Forest\nTo the West is a Lake.',
                          'North': (move, 'Cave'),
                          'East': (is_knight_there, 'Forest'),
                          'South': (move, 'Castle'),
                          'West': (move, 'Lake'),
                          'Image': 'town.png',
                          'Potion': use_potion
                        },
               
               'Cave': {'Story': 'You are at a Cave.\n\nTo the South is a Town.\n\nDo you wish to enter the Cave?',
                        'South': (move, 'Town'),
                        'Enter': (enter_cave, 'InCave'),
                        'Image': 'cave.png',
                        'Potion': use_potion
                        },
               
               'InCave': {'Story': 'The cave is dimly lit, but it may be worth searching.\n\nDo you wish to leave?',
                          'Leave': (move, 'Cave'),
                          'Search': (search_cave, 'InCave'),
                          'Image': 'dead.png',
                          'Potion': use_potion
                        },
               
               'Forest': {'Story': "You are in a Forest\n\nYou are greeted by a travelling Knight heading west\nTalk to the Knight?\n\nTo the West is a Town.",
                          'West': (move, 'Town'),
                          'Talk': (talk_to_knight, 'Knight'),
                          'Image': 'forest.png',
                          'Potion': use_potion
                        },
               
               'Knight': {'Story': 'The Knight wants to duel\n\nDo you wish to leave?',
                            'West': (move, 'Town'),
                            'Leave': (move, 'Town'),
                            # 'Fight': (health.fight, 'Knight'),
                            'Image': 'dead.png',
                            'Potion': use_potion
                        },

               'Castle': {'Story': 'You are at the Castle.\n\nTo the North is a Town.\n\nDo you wish to enter the Castle?',
                          'North': (move, 'Town'),
                          'Enter': (enter_castle, 'InCastle'),
                          'Image': 'castle.png',
                          'Potion': use_potion
                        },
               
               'InCastle': {'Story': 'A King is standing in front of you.\nTalk to the King?\n\nDo you wish to leave?',
                            'Leave': (move, 'Castle'),
                            'Talk': (talk_to_king, 'InCastle'),
                            'Image': 'castle.png',
                            'Potion': use_potion
                        },
               
               'Lake': {'Story': 'You arrive at a Lake.\n\nTo the East is a Town.',
                          'East': (move, 'Town'),
                          'Image': 'lake.png',
                          'Potion': use_potion
                        },
               }



def current_place():
    """Gets the story at the game_state place

    Returns:
        string: the story at the current place
    """
    global game_state
    
    return f"{game_places[game_state]['Story']}"

def current_status():
    
    return f"{health.status()}\n\n{current_place()}"

def game_play(user_input):
    """
    Runs the game_play

    Args:
        direction string: _North or South or East or West

    Returns:
        string: the story at the current place
    """
    global game_state

    while health.player_health > 0:
        
        story_result = ''
        valid_tokens = token.valid_list(user_input)
        if not valid_tokens:
            story_result = f"Please enter a valid command.\n\n{current_place()}"
            
        else:
            for atoken in valid_tokens:
                game_place = game_places[game_state]
                the_place = atoken.capitalize()

                if the_place in game_place:
                    health.decrease_health(5)
                    place = game_place[the_place]
                    story_result = place[0](place)
                else:
                    story_result = f"You can not do that from here.\n\n{current_place()}"            
                    
        return story_result
