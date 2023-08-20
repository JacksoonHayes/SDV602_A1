"""
This module handles the main functionalities of the game. GUI, buttons and what they do.
"""

import copy
import PySimpleGUI as sg

import cmd_parser.command_manager as cm
import inventory.inv as inventory
from status import health

# Create a deep copy of the original game's story structure for restart purposes
original_story = copy.deepcopy(cm.game_places)


def restart_game():
    """
    Resets the game to its original state.
    """
    # Reset player health to 100
    health.player_health = 100
    # Clear the inventory excluding the torch
    inventory.clear_inventory()
    # Reset the game state to the starting point
    cm.game_state = game_state = 'Cave'
    

    # Restore the original story to game places
    for place in cm.game_places:
        cm.game_places[place]['Story'] = original_story[place]['Story']
    


def make_a_window():
    """
    Initializes and returns the main game window.

    Returns:
        window: A PySimpleGUI window object representing the game window.
    """
    # Set the theme for the window
    sg.theme('Dark Brown 6')
    # Define the input area for the game commands
    prompt_input = [sg.Text('Enter your command', font='Any 14'), sg.Input(
        key='-IN-', size=(40, 1), font='Any 14')]
    # Define buttons for the game
    buttons = [
        sg.Button('Inventory'),
        sg.Button('Enter', bind_return_key=True),
        sg.Button('Restart')]
    # Group the input and buttons into a column
    command_col = sg.Column([prompt_input, buttons], element_justification='r')
    # Create the layout for the window
    layout = [
        [
            sg.Image(
                r'images/cave.png',
                size=(
                    175,
                    175),
                key="-IMG-"),
            sg.Text(
                cm.current_status(),
                size=(
                    100,
                    10),
                font='Any 12',
                key='-OUTPUT-')],
        [command_col]]

    # Return the initialized window
    return sg.Window('Adventure Game', layout, size=(600, 275))


# This ensures the code below is executed only when this script is run directly
if __name__ == "__main__":
    # Create the main game window
    window = make_a_window()

    # Event loop to keep the window running and listen for events
    while True:
        event, values = window.read()
        print(event)

        if event == 'Restart':
            # Restart the game if the "Restart" button is clicked
            restart_game()
            window['-OUTPUT-'].update(cm.current_status())
            window['-IMG-'].update(r'images/cave.png', size=(175, 175))
            window['-IN-'].update(disabled=False)

        elif health.player_health <= 0:
            # Handle player death scenario
            window['-OUTPUT-'].update(
                "Your health has reached 0 and you have died.\n\nGame Over.")
            window['-IN-'].update(disabled=True)
            window['-IMG-'].update(r'images/dead.png', size=(175, 175))

        elif event == 'Enter':
            # Handle when a command is entered and the "Enter" button is clicked
            current_story = cm.game_play(values['-IN-'].lower())
            window['-OUTPUT-'].update(current_story)
            window['-IMG-'].update(r'images/' + cm.game_places[cm.game_state]
                                   ['Image'], size=(175, 175))

        elif event == 'Inventory':
            # Toggle between showing the inventory and the current status
            if window['-OUTPUT-'].get() == inventory.show_inventory():
                window['-OUTPUT-'].update(cm.current_status())
            else:
                window['-OUTPUT-'].update(inventory.show_inventory())

        elif event is None or event == sg.WIN_CLOSED:
            # Break the event loop if the window is closed
            break

    # Close the window after exiting the event loop
    window.close()
