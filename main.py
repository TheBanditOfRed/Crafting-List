import csv
import yaml




print("")
print("")
print("")
print(" ___________________________________________________________________________________________")
print('|   _____            __ _   _                _____      _            _       _              |')
print('|  / ____|          / _| | (_)              / ____|    | |          | |     | |             |')
print('| | |     _ __ __ _| |_| |_ _ _ __   __ _  | |     __ _| | ___ _   _| | __ _| |_ ___  _ __  |')
print("| | |    | '__/ _` |  _| __| | '_ \ / _` | | |    / _` | |/ __| | | | |/ _` | __/ _ \| '__| |")
print("| | |____| | | (_| | | | |_| | | | | (_| | | |___| (_| | | (__| |_| | | (_| | || (_) | |    |")
print("|  \_____|_|  \__,_|_|  \__|_|_| |_|\__, |  \_____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|    |")
print("|                                    __/ |                                                  |")
print("|                                   |___/                                                   |")
print("|___________________________________________________________________________________________|")
print("")
print("")
print("")

with open("resources.yaml", "r") as yaml_file:
    resources = yaml.safe_load(yaml_file)

with open('testing/test.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    next(csv_reader)
    
    for row in csv_reader:
        item = row[0]
        amount = row[1]
        #dict_item = resources["resources"][item]
        print("")
        print(item)
        print("Select Process:")
        recipe_type = resources['resources'][item]['recipes']
        #print(recipe_type)
        for x in range(len(resources['resources'][item]['recipes'])):
            recipe_type = resources['resources'][item]['recipes'][x].get("recipe_type")
            print(x + 1, ". ", recipe_type)
            
        recipe_selection = input('> ')
        
        if recipe_selection.isnumeric():
            recipe_selection = int(recipe_selection)
        else:
            while recipe_selection.isnumeric() == False:
                print("Invalid Entry")
                recipe_selection = input('> ')
                if recipe_selection.isnumeric() == True:
                    recipe_selection = int(recipe_selection)
                    break
        
        while recipe_selection < 1 or recipe_selection > (len(resources['resources'][item]['recipes']) + 1) == True:
            print("Invalid Entry")
            recipe_selection = input('> ')
            if recipe_selection.isnumeric():
                recipe_selection = int(recipe_selection)
            else:
                if recipe_selection.isnumeric() == False:
                    print("Invalid Entry")
                    recipe_selection = input('> ')
                    if recipe_selection.isnumeric() == True:
                        recipe_selection = int(recipe_selection)
            if recipe_selection > 1 and recipe_selection < (len(resources['resources'][item]['recipes']) + 1):
                break
            
        
            