"""
This module processes input strings for a game, extracting valid command tokens
from the input. It ensures that player inputs are recognized and translated
into appropriate game commands.
"""

# Defines a list of recognized user inputs.
_vocab_tokens = [
    'north',
    'south',
    'east',
    'west',
    'fight',
    'potion',
    'enter',
    'leave',
    'search',
    'talk'
]


def valid_list(p_input_string):
    """
    Processes an input string and extracts valid command tokens from it.
    It splits the string by whitespace and checks if each word is a recognized command.

    Args:
        p_input_string (string): A space-separated string of potential command tokens.

    Returns:
        list: A list of recognized command tokens in the order they appeared in the input string.
    """

    # Initialize an empty list to hold valid tokens.
    result = []

    # Split the input string by whitespace and iterate over each word.
    for astring in p_input_string.split():
        # Convert the word to lowercase and check if it's a recognized command.
        if astring.lower() in _vocab_tokens:
            result.append(astring)  # If recognized, add to the result list.

    return result


if __name__ == "__main__":
    while True:
        user_input = input("Enter your game commands (or 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        recognized_commands = valid_list(user_input)
        if recognized_commands:
            print(f"Recognized commands: {recognized_commands}")
        else:
            print("No valid commands recognized. Try again.")
