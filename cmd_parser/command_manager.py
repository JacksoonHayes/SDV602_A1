import status.health as health
import time 
import inventory.inv as inventory

# Brief comment about how the following lines work
game_state = 'Town'
game_places = {'Town': {'Story': 'You are in a Town.\n\nTo the North is a Cave.\nTo the South is a Castle.\nTo the East is a Forest\nTo the West is a Lake.',
                          'North': 'Cave', 'South': 'Castle', 'East': 'Forest', 'West': 'Lake', 'Image': 'town.png'},
               
               'Cave': {'Story': 'You are at the Cave.\n\nTo the South is Forest.\n\nDo you wish to enter the Cave?',
                        'North': '', 'East': '', 'South': 'Town', 'West': '', 'Enter': 'Cave_inside', 'Image': 'cave.png'},
               
               'Castle': {'Story': 'You are at the Castle.\n\nTo the North is a Town.\n\nDo you wish to enter the Castle?',
                          'North': 'Town', 'East': '', 'South': '', 'West': '', 'Enter': 'Castle_inside', 'Image': 'castle.png'},
               
               'Forest': {'Story': 'You enter a Forest.\n\nTo the West is a Town.',
                          'North': '', 'East': '', 'South': '', 'West': 'Town', 'Image': 'forest.png'},
               
               'Lake': {'Story': 'You arrive at a Lake.\n\nTo the East is a Town.',
                          'North': '', 'East': 'Town', 'South': '', 'West': '',  'Image': 'lake.png'},
               }


def show_current_place():
    """Gets the story at the game_state place

    Returns:
        string: the story at the current place
    """
    global game_state
    
    return f"{health.show_health()}       {inventory.inv_count()}\n\n{game_places[game_state]['Story']}"


def game_play(direction):
    """
    Runs the game_play

    Args:
        direction string: _North or South or East or West

    Returns:
        string: the story at the current place
    """
    global game_state

    while health.player_health > 0:
        
        if direction.lower() in 'northeastsouthwest':  # is this a nasty check?
            game_place = game_places[game_state]
            proposed_state = game_place[direction.capitalize()]
            if proposed_state == '':
                return 'You can not go that way.\n\n'+game_places[game_state]['Story']
            else:
                game_state = proposed_state
                health.player_health -= 5
                return f"{health.show_health()}       {inventory.inv_count()}\n\n{game_places[game_state]['Story']}"

