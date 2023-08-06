import PySimpleGUI as sg

def show_inventory():
    inv_window = sg.popup('Inventory')
    inventory = cm.game_state['Inventory']
    return inv_window
    
