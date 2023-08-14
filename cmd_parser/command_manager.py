import status.health as health
import inventory.inv as inventory
import cmd_parser.token as token



def move(game_place):
    global game_state
    
    game_state = game_place[1]
    return current_place()


def enter_cave(game_place):
    result = ''
    if inventory.has_item('Torch'):
        result = move(game_place)
    else:
        result = f"You need a torch to enter the cave.\n\n{game_places[game_state]['Story']}"
    return result

def search_cave(game_place):
    if inventory.has_item('Sword'):
        return f"You find nothing of interest.\n\n{game_places[game_state]['Story']}"
    else:
        inventory.collect_item('Sword')
        game_places[game_state]['Story'] = 'You are inside the cave\n\nDo you wish to leave?'
        return f"You find a dull sword!\n\n{game_places[game_state]['Story']}"
    

def enter_castle(game_place):
    result = ''
    if inventory.has_item('Key'):
        result = move(game_place)
    else:
        result = f"A key is needed to enter the castle.\nPerhaps the man in the forest can help.\n\n{game_places[game_state]['Story']}"
    return result

def talk_to_knight(game_place):
    if inventory.has_item('Shield') or inventory.has_item('Potion'):
        return f"The knight does not speak\n\n{game_places[game_state]['Story']}"
    else:
        inventory.collect_item('Shield')
        inventory.collect_item('Potion')
        game_places[game_state]['Story'] = 'You are inside the castle\n\nDo you wish to leave?'
        return f"The knight speaks of a bounty at the nearby lake,\nyou recieve a shield and potion.\n\n{game_places[game_state]['Story']}"
    


# Brief comment about how the following lines work
game_state = 'Town'
game_places = {'Town': {'Story': 'You are in a Town.\n\nTo the North is a Cave.\nTo the South is a Castle.\nTo the East is a Forest\nTo the West is a Lake.',
                          'North': (move, 'Cave'),
                          'East': (move, 'Forest'),
                          'South': (move, 'Castle'),
                          'West': (move, 'Lake'),
                          'Image': 'town.png'
                          },
               
               'Cave': {'Story': 'You are at a Cave.\n\nTo the South is a Town.\n\nDo you wish to enter the Cave?',
                        'South': (move, 'Town'),
                        'Enter': (enter_cave, 'InCave'),
                        'Image': 'cave.png'
                        },
               
               'InCave': {'Story': 'The cave is dimly lit, but it may be worth searching\n\nDo you wish to leave?',
                                'Leave': (move, 'Cave'),
                                'Search': (search_cave, 'InCave'),
                                'Image': 'dead.png'
                            },
               
               'Forest': {'Story': 'You enter a Forest.\n\nTo the West is a Town.',
                          'West': (move, 'Town'),
                          'Image': 'forest.png'
                          },

               'Castle': {'Story': 'You are at the Castle.\n\nTo the North is a Town.\n\nDo you wish to enter the Castle?',
                          'North': (move, 'Town'),
                          'Enter': (enter_castle, 'InCastle'),
                          'Image': 'castle.png'
                        },
               
               'InCastle': {'Story': 'You are greated by a knight\nTalk to the knight?\n\nDo you wish to leave?',
                            'Leave': (move, 'Castle'),
                            'Talk': (talk_to_knight, 'InCastle'),
                            'Image': 'castle.png'
                        },
               
               'Lake': {'Story': 'You arrive at a Lake.\n\nTo the East is a Town.',
                          'East': (move, 'Town'),
                          'Image': 'lake.png'
                          },
               }



def current_place():
    """Gets the story at the game_state place

    Returns:
        string: the story at the current place
    """
    global game_state
    
    return f"{health.status()}\n\n{game_places[game_state]['Story']}"

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
            story_result = f"PLEASE ENTER A VALID COMMAND\n\n{game_places[game_state]['Story']}"
            
        else:
            for atoken in valid_tokens:
                game_place = game_places[game_state]
                the_place = atoken.capitalize()

                if the_place in game_place:
                    health.decrease_health(5)
                    place = game_place[the_place]
                    story_result = place[0](place)
                else:
                    story_result = f"You can not go {atoken} from here\n\n{game_places[game_state]['Story']}"            
                    
        return story_result
