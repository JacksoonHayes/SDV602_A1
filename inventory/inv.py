import PySimpleGUI as sg
import cmd_parser.command_manager as cm


player_inventory = set()

def collect_item(item):
    player_inventory.add(item)

def has_item(item):
    return item in player_inventory

def show_inventory():
    return (f"Inventory: \n{player_inventory}")
    
