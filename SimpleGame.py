""" 
A comment describing the game module
"""
import PySimpleGUI as sg
import time
import cmd_parser.token as token
import cmd_parser.command_manager as cm
import inventory.inv as inventory
import status.health as health


def make_a_window():
    """
    Creates a game window

    Returns:
        window: the handle to the game window
    """

    sg.theme('Dark Brown 6')  # please make your windows
    prompt_input = [sg.Text('Enter your command', font='Any 14'), sg.Input(
        key='-IN-', size=(40, 1), font='Any 14')]
    buttons = [sg.Button('Inventory'), sg.Button('Status'), sg.Button('Enter',  bind_return_key=True), sg.Button('Exit')]
    command_col = sg.Column([prompt_input, buttons], element_justification='r')
    layout = [[sg.Image(r'images/town.png', size=(175, 175), key="-IMG-"), sg.Text(cm.show_current_place(), size=(100, 8), font='Any 12', key='-OUTPUT-')],
              [command_col]]

    return sg.Window('Adventure Game', layout, size=(600, 260))


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
        if event == 'Enter':
            list_of_tokens = token.valid_list(values['-IN-'].lower())

            for atoken in list_of_tokens:
                current_story = cm.game_play(atoken)
                window['-OUTPUT-'].update(current_story)

            window['-IMG-'].update(r'images/'+cm.game_places[cm.game_state]
                                   ['Image'], size=(175, 175))

            pass
        
        elif event == 'Inventory':
            window['-OUTPUT-'].update(inventory.show_inventory())
            
        elif event == 'Status':
            window['-OUTPUT-'].update(health.show_status())
            
        elif event == 'Exit' or event is None or event == sg.WIN_CLOSED:
            break
        
        else:
            pass


    window.close()
