#classes are for:
#bundling related data
#with the functions that modify that data

from random import randint

class Cat:
    #in __init__ python is refering to itself as it is being created

    def __init__(self, new_name, friendiness=0.5, happiness=10, cuddle_power=1):
        self.name = new_name
        self.friendliness = friendiness
        self.happiness = happiness
        self.cuddle_power = cuddle_power

    def greet(self, whom):
        print(f'Hello I am {self.name}. Nice to meet you {whom.name}')

    def cuddle(self, whom):
        cuddle__chance = randint(0,10)/10
        if cuddle__chance <= self.friendliness:
            print(f'I cuddle you, {whom.name}')
            whom.happiness += self.cuddle_power
        else:
            print(f'Leave me alone, {whom.name}')

 # use class to make a new instance of Cat, or a new Cat instance
othercat = Cat('Milla')
mycat = Cat('Oakley')

class CuddlyCat(Cat):
    




# class Car:
#     def __init__(self, year, make, model, is_bitchin='yes'):
#         self.year = year
#         self.make = make
#         self.model = model
#         self.is_bitchin = is_bitchin
#         if make != 'Toyota' and model != 'Tacoma':
#             print(make != 'Toyota')
#             print(model != 'Tacoma')
#             self.is_bitchin = 'No'

# nelly = Car(2012, 'Toyota', 'Tacoma', 'yes')
# veronica = Car(2007, 'Toyota', '4runner')