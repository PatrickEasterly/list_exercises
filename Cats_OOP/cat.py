#classes are for:
#bundling related data
#with the functions that modify that data

##### Buzzwords
#Encapsulation - hiding the details about how something is done (usually inside of methods)
#Encapsulation, alternate - bundling related data along with functions that use and modify
# that data

#Inheritance - making specialized classes based on other classes

#Polymorphism - methods can interact with different kinds of objects and it doesn't care what 
# class created it

#Composition - not stuffing everything into a single class. 
# instead, make classes that help other classes. 
# Create specialized objects that cooperate with each other



from random import randint

class Cat:
    #in __init__ python is refering to itself as it is being created
    def __init__(self, new_name, friendiness=0.5, happiness=10, cuddle_power=1):
        self.name = new_name
        self.friendliness = friendiness
        self.happiness = happiness
        self.cuddle_power = cuddle_power

    def recieve_toy(self, toy):
        self.toy = toy

    def play_with_toy(self):
        #this increases happiness
        print(f'{self.name} plays with {self.toy.name}')
        self.happiness += self.toy.quality
        

    def greet(self, whom):
        print(f'Hello I am {self.name}. Nice to meet you {whom.name}')

    def cuddle(self, whom):
        cuddle__chance = randint(0,10)/10
        if cuddle__chance <= self.friendliness:
            #as long as 'whom' has a .name and a .happiness, cuddle method works
            #when a method can interact with many different kinds of objects, 
            #that's called 'Polymorphism'
            print(f'I cuddle you, {whom.name}')
            whom.happiness += self.cuddle_power
        else:
            print(f'Leave me alone, {whom.name}')

 # use class to make a new instance of Cat, or a new Cat instance
othercat = Cat('Milla')
mycat = Cat('Oakley')





class Car:
    def __init__(self, year, make, model, best='yes'):
        
        self.year = year
        self.make = make
        self.model = model
        self.best = best
        if make != 'Toyota' or model != 'Tacoma':
            self.best = 'No'

nelly = Car(2012, 'Toyota', 'Tacoma', 'yes')
veronica = Car(2007, 'Toyota', '4runner')
