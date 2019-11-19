puppy = {
    "name": "Cujo",
    "fullness": 50,
    "happiness": 20,
}

# Define functions that increase a pet's attribute levels.
def feed_pet(pet):
    pet["fullness"] += 10

def play_with_pet(pet):
    pet["happiness"] += 10

# Decrease a pet's attribute levels.    
def get_hungry_and_mopey(pet):
    pet["fullness"] -= 5
    pet["happiness"] -= 5

# Prompt the user to interact with the pet
while True:

    print("""
%s's stats:
Fullness: %d
Happiness: %d
""" % (puppy["name"], puppy["fullness"], puppy["happiness"]))
    
    choice = int(input("""
1. Feed puppy
2. Play with puppy
3. Do nothing
"""))
    if choice == 1:
        feed_pet(puppy)
    elif choice == 2:
        play_with_pet(puppy)
    else:
        pass

    # Each time the loop runs, the pet
    # will need some attention!
    get_hungry_and_mopey(puppy)