import yaml
import getpass
import random

with open("game-config.yml", "r") as f:
    config = yaml.safe_load(f)
    
range_min = config['range']['min']
range_max = config['range']['max']
guess_allowed = config['guesses']
mode = config['mode']

solved = False

if mode == "single":
    correct_number = random.randint(range_min, range_max)
elif mode == "multi":
    correct_number = int(getpass.getpass("P2 Guess: "))
else:
    print("Invalid config")
    exit()
    
for i in range(guess_allowed):
    guess = int(input("enter guess"))
    
    if guess == correct_number:
        print(f"COrrect you needed {i + 1} tries")
        solved = True
        break
    elif guess < correct_number:
        print("too low")
    else:
        print("too high")
        
if not solved:
    print("you lost, correct was", correct_number)