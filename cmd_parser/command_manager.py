import status.health as health
import inventory.inv as inventory
import cmd_parser.token as token



def move(game_place):
    
    global game_state

    game_state = game_place[1]

    return current_place()

# Brief comment about how the following lines work
game_state = 'Town'
game_places = {'Town': {'Story': 'You are in a Town.\n\nTo the North is a Cave.\nTo the South is a Castle.\nTo the East is a Forest\nTo the West is a Lake.',
                          'North': (move, 'Cave'),
                          'East': (move, 'Forest'),
                          'South': (move, 'Castle'),
                          'West': (move, 'Lake'),
                          'Image': 'town.png'
                          },
               
               'Cave': {'Story': 'You are at the Cave.\n\nTo the South is a Town.\n\nDo you wish to enter the Cave?',
                        'South': (move, 'Town'),
                        'Enter': (move, 'InCave'),
                        'Image': 'cave.png'
                        },
               
               'InCave': {'Story': 'You are inside the Cave.\n\nDo you wish to leave?',
                                'Leave': (move, 'Cave'),
                                'Item': 'Sword',
                                'Image': 'dead.png'
                            },
               
               'Forest': {'Story': 'You enter a Forest.\n\nTo the West is a Town.',
                          'West': (move, 'Town'),
                          'Image': 'forest.png'
                          },

               'Castle': {'Story': 'You are at the Castle.\n\nTo the North is a Town.\n\nDo you wish to enter the Castle?',
                          'North': (move, 'Town'),
                          'Enter': (move, 'InCastle'),
                          'Image': 'castle.png'
                        },
               
               'InCastle': {'Story': 'You are inside the Castle.\n\nDo you wish to leave the Castle?',
                            'Leave': (move, 'Castle'),
                            'Item': 'Shield',
                            'Image': 'castle.png'
                        },
               
               'Lake': {'Story': 'You arrive at a Lake.\n\nTo the East is a Town.',
                          'East': (move, 'Town'),
                          'Image': 'lake.png'
                          },
               }


def item_check():
     if 'Item' in game_places[game_state]:
        item = game_places[game_state]['Item']
        if item and item not in inventory.player_inventory:
            inventory.collect_item(item)



def current_place():
    """Gets the story at the game_state place

    Returns:
        string: the story at the current place
    """
    global game_state
    
    return f"{health.show_health()}       {inventory.inv_count()}\n\n{game_places[game_state]['Story']}"

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
                if item_check():
                    item = game_places[game_state]['Item']
                    story_result = f"You found a {item}!\n\n{game_places[game_state]['Story']}"
                elif the_place in game_place:
                    health.decrease_health(5)
                    place = game_place[the_place]
                    story_result = place[0](place)
                else:
                    story_result = f"You can not go {atoken} from here\n\n{game_places[game_state]['Story']}"            
                    
        return story_result
