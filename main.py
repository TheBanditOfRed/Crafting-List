# no mater how dumb you think people are, they will still find a way to surprise you

import csv
import tkinter as tk
from tkinter import filedialog
import json
import math
import os

root = tk.Tk()
#check and create required folders if missing
os.makedirs('saved-process/', exist_ok=True)
os.makedirs('material-lists/', exist_ok=True)

# Load main files
with open("config.json", "r") as config_json:
    config = json.load(config_json)


with open("resources.json", "r") as resources_json:
    resources = json.load(resources_json)


def startup_icon():
    print("")
    print("")
    print("")
    print(" ___________________________________________________________________________________________")
    print("|                                                                                           |")
    print('|   _____            __ _   _                _____      _            _       _              |')
    print('|  / ____|          / _| | (_)              / ____|    | |          | |     | |             |')
    print('| | |     _ __ __ _| |_| |_ _ _ __   __ _  | |     __ _| | ___ _   _| | __ _| |_ ___  _ __  |')
    print(r"| | |    | '__/ _` |  _| __| | '_ \ / _` | | |    / _` | |/ __| | | | |/ _` | __/ _ \| '__| |")
    print("| | |____| | | (_| | | | |_| | | | | (_| | | |___| (_| | | (__| |_| | | (_| | || (_) | |    |")
    print(r"|  \_____|_|  \__,_|_|  \__|_|_| |_|\__, |  \_____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|    |")
    print("|                                    __/ |                                                  |")
    print("|                                   |___/                         Created by TheBanditOfRed |")
    print("|                                                                Assisted by conallkavanagh |")
    print("|___________________________________________________________________________________________|")#15
    print("")
    print("")
    print("")

def data_format():
    data = {
        'item': '',
        'process': '',
        'multiplier': '',
    }

def add_new_item():
    print('To be done')
    root.mainloop(
        startup_icon(),
        menu(resources, config)
    )

def settings(config, resources):
    #WIP

    defaults = config['Defaults']
    default_item_num = 0
    default_selection_options = []

    # Creating option screen
    for key, value in defaults.items():
        default_selection_options.append(key)
        buffer = max(len(key) for key, value in defaults.items()) + 10
        default_item_num = default_item_num + 1
        if default_item_num % 2 != 0:
            spaced_key = key + " [" + str(default_item_num) + "]"
            print(spaced_key.ljust(buffer), end="")
        elif default_item_num % 2 == 0:
            print(key + " [" + str(default_item_num) + "]")
    if default_item_num % 2 != 0:
        print("")
    print("")

    # Option Selection
    config_selection = input('> ')
                
    # Invalid entry handeling
    while config_selection.isnumeric() == False or not 1 <= int(config_selection) <= len(defaults) + 1:
        print(f"Invalid Entry: Please enter a number from 1 to {len(defaults) + 1}")
        config_selection = input('> ')
    print(config_selection)

    config_selection = int(config_selection) - 1
    print("Current", default_selection_options[config_selection].lower(), ": ", resources["requirement_groups"][default_selection_options[config_selection].replace("Default", "Any")][defaults[default_selection_options[config_selection]]])


def crafting_calculator(resources, config, path, save_file_path):
    with open("config.json", "r") as config_json:
        config = json.load(config_json)
    return

def process_selection(resources, config, path, save_file_path):
    try:
        with open(path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            
            for row in csv_reader:
                item = row[0]
                amount = int(row[1])
                
                stack_size = 64         # Will be defined via config file when I get to it
                
                # Better amount readibilty maths
                num_stacks = math.trunc(amount / stack_size)
                num_items = amount - (num_stacks * stack_size)
                
                print("")
                if num_stacks == 1:
                    print(item, ": ", num_stacks, "Stack +", num_items)
                else:
                    print(item, ": ", num_stacks, "Stacks +", num_items)
                        
                    
                print("Select Process:")
                try:
                    recipes = resources['resources'][item]['recipes']
                except:
                    print("The following item", item, "does not exist in resources.json")
                    print("Would you like to add it? (Y/N)")
                    add_new_item_input = input("> ")
                    add_new_item_input = add_new_item_input.lower().strip('eso')
                    while add_new_item_input not in ['y', 'n']:
                        print("Invalid Entry: Please select [Y]es or [N]o")
                        add_new_item_input = input('> ')
                        add_new_item_input = add_new_item_input.lower().strip('es')
                    if add_new_item_input == 'y':
                        add_new_item(item)
                    elif add_new_item_input == 'n':
                        print('Would you like to [S]kip this item, or return to the [M]enu')
                        add_new_item_input = input('> ')
                        add_new_item_input = add_new_item_input.lower().strip('kipenu')
                        while add_new_item_input not in ['s', 'm']:
                            print("Invalid Entry: Please select [S]kip or [M]enu")
                            add_new_item_input = input('> ')
                            add_new_item_input = add_new_item_input.lower().strip('kipenu')
                        if add_new_item_input == 's':
                            continue
                        elif add_new_item_input == 'm':
                            root.mainloop(
                                startup_icon(),
                                menu(resources, config)
                                )
                
                for x in range(len(recipes)):
                    recipe_type = recipes[x].get("recipe_type")

                    amount_recipe_type = {}
                    
                    amount_pros = 0
                    multiplier = 0

                    if recipe_type == "Raw Resource":
                        amount_pros = amount
                    else:
                        while amount_pros < amount:
                            amount_pros = amount_pros + recipes[x].get("output")
                            multiplier = multiplier + 1

                    amount_recipe_type[recipe_type] = amount_pros
                    
                    # Better amount readibilty maths
                    num_stacks_pros = math.trunc(amount_pros / stack_size)
                    num_items_pros = amount_pros - (num_stacks_pros * stack_size)
                    
                    if num_stacks_pros == 1:
                        print("[" + str(x + 1) + "]", recipe_type, ": ", num_stacks_pros, "Stack +", num_items_pros)
                    else:
                        print("[" + str(x + 1) + "]", recipe_type, ": ", num_stacks_pros, "Stacks +", num_items_pros)
                    
                recipe_selection = input('> ')
                
                # Invalid entry handeling
                while recipe_selection.isnumeric() == False or not 1 <= int(recipe_selection) <= len(recipes):
                    print(f"Invalid Entry: Please enter a number from 1 to {len(recipes)}")
                    recipe_selection = input('> ')
            
                recipe_selection = int(recipe_selection) - 1

                with open(save_file_path) as file_path:
                    add_processes = json.load(file_path)

                add_processes.append({
                    "Item": item,
                    "Amount": amount_pros,
                    "Process": recipe_selection
                })

                #print(add_processes)

                with open(save_file_path, 'w') as json_file:
                    json.dump(add_processes, json_file,
                            indent=4,
                            separators=(',',': '))
                    
            #file "saving" (more properly file deleting but makes more sense to the user this way)
            print("Save process selection? (Y/N)")
            file_save_selection = input('> ')
            file_save_selection = file_save_selection.lower().strip('eso')
            while file_save_selection not in ['y', 'n']:
                print("Invalid Entry: Please select [Y]es or [N]o")
                file_save_selection = input('> ')
                file_save_selection = file_save_selection.lower().strip('es')
            if file_save_selection == 'y':
                print(r"File saved to ~\saved-process")
            elif file_save_selection == 'n':
                print('Are you sure you want to delete the process list? (Y/N)')
                file_save_selection = input('> ')
                file_save_selection = file_save_selection.lower().strip('eso')
                while file_save_selection not in ['y', 'n']:
                    print("Invalid Entry: Please select [Y]es or [N]o")
                    file_save_selection = input('> ')
                    file_save_selection = file_save_selection.lower().strip('es')
                if file_save_selection == 'y':
                    os.remove(save_file_path)
                elif file_save_selection == 'n':
                    print(r"File saved to ~\saved-process")
            
            root.mainloop(
                startup_icon(),
                menu(resources, config)
                )
                
    except:
        print("No material list selected")
        print("Returning to menu")
        root.mainloop(
            startup_icon(),
            menu(resources, config)
            )

def load(save_file_path):
    print('To be done')
    root.mainloop(
        startup_icon(),
        menu(resources, config)
        )

def menu(resources, config):
    print("|   [1] Start Calculation   |   [2] Settings   |   [3] Load Crafting List   |   [4] Exit   |")
    menu_sel = input("> ")
    
    # Invalid entry handeling
    while menu_sel.isnumeric() == False or not 1 <= int(menu_sel) <= 4:
        print("Invalid Command")
        menu_sel = input('> ')
        
    menu_sel = int(menu_sel)
                    
    if menu_sel == 1:
        path = filedialog.askopenfilename(
            defaultextension = '~\AppData\Roaming\.minecraft\config\litematica',
            filetypes = [("CSV Files", "*.csv")]
        )
        basename = os.path.basename(path) 
        material_list_name, _ = os.path.splitext(basename) 
        save_file_name = material_list_name + '.json'
        save_file_path = 'saved-process/' + save_file_name
        print(save_file_name)
        print(save_file_path)
        #check if new_process_selection.json already exists
        try:
            new_process_selection_json = open('saved-process/new_process_selection.json', 'x')
            new_process_selection_json.close()

            new_process_selection_json_setup = [
                {
                    "Material List": material_list_name,
                    "Path": path
                },
            ]

            with open('saved-process/new_process_selection.json', 'w') as new_process_selection_json:
                json.dump(new_process_selection_json_setup, new_process_selection_json,
                          indent=4,
                          separators=(',',': '))
            new_process_selection_json.close()
        except:
            print('Found existing startup file')
            os.remove('saved-process/new_process_selection.json')
            print('Existing startup file deleted')
            new_process_selection_json = open('saved-process/new_process_selection.json', 'x')
            new_process_selection_json.close()

            new_process_selection_json_setup = [
                {
                    "Material List": save_file_name,
                    "Path": path
                },
            ]

            with open('saved-process/new_process_selection.json', 'w') as new_process_selection_json:
                json.dump(new_process_selection_json_setup, new_process_selection_json,
                          indent=4,
                          separators=(',',': '))
            new_process_selection_json.close()
            print('Created new startup file')
        try:
            os.rename('saved-process/new_process_selection.json', save_file_path)
        except:
            print("It looks like there might already be a crafting list for this file")
            print("Would you like to [L]oad the existing Crafting List, or create a [N]ew Crafting List?")
            existing_list_input = input("> ")
            existing_list_input = existing_list_input.lower().strip('oadew')
            while existing_list_input not in ['l', 'n']:
                print("Invalid Entry: Please select [L]oad or [N]ew file")
                existing_list_input = input('> ')
                existing_list_input = existing_list_input.lower().strip('oadew')
            if existing_list_input == 'l':
                load(save_file_path)
            elif existing_list_input == 'n':
                print(r'Would you like to delete the existing list? (Y\N)')
                existing_list_input = input('> ')
                existing_list_input = existing_list_input.lower().strip('eso')
                while existing_list_input not in ['y', 'n']:
                    print("Invalid Entry: Please select [Y]es or [N]o")
                    existing_list_input = input('> ')
                    existing_list_input = existing_list_input.lower().strip('eso')
                if existing_list_input == 'y':
                    os.remove(save_file_path)
                    os.rename('saved-process/new_process_selection.json', save_file_path)
                elif existing_list_input == 'n':
                    file_rename_input = input("Rename file to:  ")
                    invalid_characters = r'*?:"<>\/|'
                    while any(c in invalid_characters for c in file_rename_input) == True:
                        print('New name can not contain the following charachters:   ', invalid_characters)
                        file_rename_input = input('Please enter valid file name:   ')
                    while file_rename_input == material_list_name:
                        print('New name can not be the same as the orignal file')
                        file_rename_input = input('Please enter valid file name:   ')
                        while any(c in invalid_characters for c in file_rename_input) == True:
                            print('New name can not contain the following charachters:   ', invalid_characters)
                            file_rename_input = input('Please enter valid file name:   ')
                    if "." in file_rename_input:            #user input file extension handling
                        material_list_name, _ = os.path.splitext(file_rename_input)
                    else:
                        material_list_name = file_rename_input
                    save_file_name = material_list_name + '.json'
                    save_file_path = 'saved-process/' + save_file_name
                    print(save_file_name)
                    print(save_file_path)
                    try:
                        os.rename('saved-process/new_process_selection.json', save_file_path)
                    except:
                        print("An error ocured:   FILE WITH SAME NAME ALREADY EXISTS")
                        print("Returning to menu")
                        root.mainloop(
                            startup_icon(),
                            menu(resources, config)
                            )

                        
        process_selection(resources, config, path, save_file_path)
    elif menu_sel == 2:
        settings(config, resources)
        print("DO ADD ITEM")
    elif menu_sel == 3:
        print("DO FILE LOADING")
    elif menu_sel == 4:
        os._exit(1)

root.withdraw()
root.attributes("-topmost", True)
root.mainloop(
    startup_icon(),
    menu(resources, config)
    )   