from cat import Cat
from random import randint
# it's a new class of cat, with all of cat's attributes, plus whatever else you add
# CuddlyCat is a subclass of Cat, and Cat is the superclass of CuddlyCat

class CuddlyCat(Cat):
    def __init__(self, new_name):
        super().__init__(new_name, 0.9, 50, 5)

    def cuddle(self, whom):
        cuddle_chance = randint(0, 10)/10
        if cuddle_chance <= self.friendliness:
            print(f'I cuddle you, {whom.name}!')
            whom.happiness *= self.cuddle_power
        else:
            print(f'Bad touch! Bad touch!')
    
artemis = CuddlyCat('Artie')
