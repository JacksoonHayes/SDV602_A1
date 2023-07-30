

# Brief comment about how the following lines work
game_state = 'Forest'
game_places = {'Forest': {'Story': 'You are in the Forest\n\nTo the North is a Cave.\nTo the South is a Castle.\nTo the East is a Town\nTo the West is a Lake.',
                          'North': 'Cave', 'South': 'Castle', 'East': 'Town', 'West': 'Lake', 'Image': 'forest.png'},
               
               'Cave': {'Story': 'You are at the Cave.\n\nTo the South is Forest.\nTo the East is a Town.\nTo the West is a Lake.',
                        'North': '', 'South': 'Forest','East': 'Town', 'West': 'Lake', 'Image': 'cave.png'},
               
               'Castle': {'Story': 'You are at the Castle.\n\nTo the North is forest.\nTo the East is a Town.\nTo the West is a Lake.',
                          'North': 'Forest', 'South': '','East': 'Town', 'West': 'Lake', 'Image': 'castle.png'},
               
               'Town': {'Story': 'You enter a Town.\n\nTo the North is a Cave.\nTo the West is a Forest.\nTo the South is a Castle.',
                          'North': 'Cave', 'South': 'Castle', 'East': '', 'West': 'Forest',  'Image': 'town.png'},
               
               'Lake': {'Story': 'You arrive at a Lake.\n\nTo the North is a Cave.\nTo the East is a Forest.\nTo the South is a Castle.',
                          'North': 'Cave', 'South': 'Castle', 'East': 'Forest', 'West': '',  'Image': 'lake.png'},
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

    if direction.lower() in 'northsoutheastwest':  # is this a nasty check?
        game_place = game_places[game_state]
        proposed_state = game_place[direction.capitalize()]
        if proposed_state == '':
            return 'You can not go that way.\n'+game_places[game_state]['Story']
        else:
            game_state = proposed_state
            return game_places[game_state]['Story']

