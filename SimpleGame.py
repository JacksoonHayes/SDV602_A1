""" 
A comment describing the game module
"""
import PySimpleGUI as sg
import cmd_parser.command_manager as cm
import inventory.inv as inventory
import status.health as health
import copy

original_story = copy.deepcopy(cm.game_places)

def restart_game():
    global game_state
    health.player_health = 100
    inventory.clear_inventory()  
    game_state = 'Cave'
    
    for place in cm.game_places:
        cm.game_places[place]['Story'] = original_story[place]['Story']

def make_a_window():
    """
    Creates a game window

    Returns:
        window: the handle to the game window
    """

    sg.theme('Dark Brown 6')  # please make your windows
    prompt_input = [sg.Text('Enter your command', font='Any 14'), sg.Input(
        key='-IN-', size=(40, 1), font='Any 14')]
    buttons = [sg.Button('Inventory'), sg.Button('Enter',  bind_return_key=True), sg.Button('Restart')]
    command_col = sg.Column([prompt_input, buttons], element_justification='r')
    layout = [[sg.Image(r'images/cave.png', size=(175, 175), key="-IMG-"), sg.Text(cm.current_status(), size=(100, 10), font='Any 12', key='-OUTPUT-')],
              [command_col]]

    return sg.Window('Adventure Game', layout, size=(600, 275))


if __name__ == "__main__":
    # testing for now
    # print(show_current_place())
    # current_story = game_play('North')
    # print(show_current_place())

    # A persisent window - stays until "Exit" is pressed
    window = make_a_window()

    while True:
        event, values = window.read()
        print(event)
        
        if event == 'Restart':
            restart_game()
            window['-OUTPUT-'].update(cm.current_status())
            window['-IMG-'].update(r'images/cave.png', size=(175, 175))  # Reset to the initial image
            window['-IN-'].update(disabled=False)      
             
        if health.player_health <= 0:
            window['-OUTPUT-'].update("Your health has reached 0 and you have died.\n\nGame Over.")
            window['-IN-'].update(disabled=True)
            window['-IMG-'].update(r'images/dead.png' , size=(175, 175))
            pass
        
        elif event == 'Enter':
            current_story = cm.game_play(values['-IN-'].lower())
            window['-OUTPUT-'].update(current_story)
            window['-IMG-'].update(r'images/'+cm.game_places[cm.game_state]
                                   ['Image'], size=(175, 175))
            pass
        
        elif event == 'Inventory':
            if window['-OUTPUT-'].get() == inventory.show_inventory():
                window['-OUTPUT-'].update(cm.current_status())
            else:
                window['-OUTPUT-'].update(inventory.show_inventory())
            pass
            
        elif event is None or event == sg.WIN_CLOSED:
            break

        else:
            
            pass
        
    window.close()
