

# Brief comment about how the following lines work
game_state = 'Town'
game_places = {'Town': {'Story': 'You are in a Town.\n\nTo the North is a Cave.\nTo the South is a Castle.\nTo the East is a Forest\nTo the West is a Lake.',
                          'North': 'Cave', 'South': 'Castle', 'East': 'Forest', 'West': 'Lake', 'Image': 'town.png'},
               
               'Cave': {'Story': 'You are at the Cave.\n\nTo the South is Forest.\nTo the East is a Town.\nTo the West is a Lake.',
                        'North': '', 'South': 'Town','East': 'Forest', 'West': 'Lake', 'Image': 'cave.png'},
               
               'Castle': {'Story': 'You are at the Castle.\n\nTo the North is forest.\nTo the East is a Town.\nTo the West is a Lake.',
                          'North': 'Town', 'South': '','East': 'Forest', 'West': 'Lake', 'Image': 'castle.png'},
               
               'Forest': {'Story': 'You enter a Forest.\n\nTo the North is a Cave.\nTo the West is a Town.\nTo the South is a Castle.',
                          'North': 'Cave', 'South': 'Castle', 'East': '', 'West': 'Town',  'Image': 'forest.png'},
               
               'Lake': {'Story': 'You arrive at a Lake.\n\nTo the North is a Cave.\nTo the East is a Forest.\nTo the South is a Castle.',
                          'North': 'Cave', 'South': 'Castle', 'East': 'Town', 'West': '',  'Image': 'lake.png'},
               }


def show_current_place():
    """Gets the story at the game_state place

    Returns:
        string: the story at the current place
    """
    global game_state

    return game_places[game_state]['Story']


def game_play(direction):
    """
    Runs the game_play

    Args:
        direction string: _North or South or East or West

    Returns:
        string: the story at the current place
    """
    global game_state

    if direction.lower() in 'northeastsouthwest':  # is this a nasty check?
        game_place = game_places[game_state]
        proposed_state = game_place[direction.capitalize()]
        if proposed_state == '':
            return 'You can not go that way.\n\n'+game_places[game_state]['Story']
        else:
            game_state = proposed_state
            return game_places[game_state]['Story']

