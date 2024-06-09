import csv
import yaml
import math
import datetime


with open("resources.yaml", "r") as resources_yaml:
    resources = yaml.safe_load(resources_yaml)
    
with open("config.yaml", "r") as config_yaml:
    config = yaml.safe_load(config_yaml)


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
    print("|___________________________________________________________________________________________|")
    print("")
    print("")
    print("")
 
#will be needed at some point in future
'''if config["Display Amount"].get("Stack") == 1:
    stack_size = 64
elif config["Display Amount"].get("Shulker Box") == 1:
    stack_size = 1728
elif config["Display Amount"].get("Double Chest") == 1:
    stack_size = 3456'''

def data_format():
    data = {
        'item': '',
        'process': '',
        'multiplier': '',
    }

def process_selection(resources, config):
    #try:
        with open('mats_list/test.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            
            next(csv_reader)
            
            for row in csv_reader:
                item = row[0]
                amount = int(row[1])
                
                stack_size = 64
                
                num_stacks = math.trunc(amount / stack_size)
                num_items = amount - (num_stacks * stack_size)
                
                print("")
                if num_stacks == 1:
                    print(item, ": ", num_stacks, "Stack +", num_items)
                else:
                    print(item, ": ", num_stacks, "Stacks +", num_items)
                    
                    
                print("Select Process:")
                recipes = resources['resources'][item]['recipes']
                
                for x in range(len(recipes)):
                    recipe_type = recipes[x].get("recipe_type")
                    
                    amount_pros = 0
                    rr_amount = 0
                    s_amount = 0
                    aw_amount = 0
                    st_amount = 0
                    t_amount = 0
                    c_amount = 0
                    sh_amount = 0
                    as_amount = 0
                    cu_amount = 0
                    o_amount = 0
                    sm_amount = 0
                    cr_amount = 0
                    multiplier = 0
                    if recipe_type == "Raw Resource":
                        amount_pros = amount
                        rr_amount = amount
                    elif recipe_type == "Smelting":
                        while amount_pros < amount:
                            amount_pros = amount_pros + recipes[x].get("output")
                            multiplier = multiplier + 1
                        s_amount = amount_pros
                    elif recipe_type == "Add Water":
                        while amount_pros < amount:
                            amount_pros = amount_pros + recipes[x].get("output")
                            multiplier = multiplier + 1
                        aw_amount = amount_pros
                    elif recipe_type == "Strip":
                        while amount_pros < amount:
                            amount_pros = amount_pros + recipes[x].get("output")
                            multiplier = multiplier + 1
                        st_amount = amount_pros
                    elif recipe_type == "Till":
                        while amount_pros < amount:
                            amount_pros = amount_pros + recipes[x].get("output")
                            multiplier = multiplier + 1
                        t_amount = amount_pros
                    elif recipe_type == "Carve":
                        while amount_pros < amount:
                            amount_pros = amount_pros + recipes[x].get("output")
                            multiplier = multiplier + 1
                        c_amount = amount_pros
                    elif recipe_type == "Shovel":
                        while amount_pros < amount:
                            amount_pros = amount_pros + recipes[x].get("output")
                            multiplier = multiplier + 1
                        sh_amount = amount_pros
                    elif recipe_type == "As":
                        while amount_pros < amount:
                            amount_pros = amount_pros + recipes[x].get("output")
                            multiplier = multiplier + 1
                        as_amount = amount_pros
                    elif recipe_type == "Cutting":
                        while amount_pros < amount:
                            amount_pros = amount_pros + recipes[x].get("output")
                            multiplier = multiplier + 1
                        cu_amount = amount_pros
                    elif recipe_type == "Oxidation":
                        while amount_pros < amount:
                            amount_pros = amount_pros + recipes[x].get("output")
                            multiplier = multiplier + 1
                        o_amount = amount_pros
                    elif recipe_type == "Smithing Table":
                        while amount_pros < amount:
                            amount_pros = amount_pros + recipes[x].get("output")
                            multiplier = multiplier + 1
                        sm_amount = amount_pros
                    elif recipe_type == "Crafting":
                        while amount_pros < amount:
                            amount_pros = amount_pros + recipes[x].get("output")
                            multiplier = multiplier + 1
                        cr_amount = amount_pros
                    
                    num_stacks_pros = math.trunc(amount_pros / stack_size)
                    num_items_pros = amount_pros - (num_stacks_pros * stack_size)
                    
                    if num_stacks_pros == 1:
                        print("[" + str(x + 1) + "]", recipe_type, ": ", num_stacks_pros, "Stack +", num_items_pros)
                    else:
                        print("[" + str(x + 1) + "]", recipe_type, ": ", num_stacks_pros, "Stacks +", num_items_pros)
                    
                recipe_selection = input('> ')
                
                while recipe_selection.isnumeric() == False or not 1 <= int(recipe_selection) <= len(recipes):
                    print(f"Invalid Entry: Please enter a number from 1 to {len(recipes)}")
                    recipe_selection = input('> ')
            
                recipe_selection = int(recipe_selection) - 1
                
                
    #except:
    #    print("No material list found")
        
def menu(resources, config):
    print("|    [1] Start Calculation    |    [2] Edit Config    |    [3] Load Crafting List    |")
    menu_sel = input("> ")
    
    while menu_sel.isnumeric() == False or not 1 <= int(menu_sel) <= 3:
        print("Invalid Command")
        menu_sel = input('> ')
        
    menu_sel = int(menu_sel)
                    
    if menu_sel == 1:
        process_selection(resources, config)
    elif menu_sel == 2:
        print("DO CONFIG FILE CONFIG WHEN YOU LEARN HOW TO EDIT YAML FILES")
    elif menu_sel == 3:
        print("DO FILE LOADING WHEN YOU GET AROUND TO WRITING FILES")

startup_icon()
menu(resources, config)
