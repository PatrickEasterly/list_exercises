from Character import Character
class Hero(Character):
    def __init__(self):
        self.health = 10
        self.power = 5
        self.type = 'Hero'
    def attack(self, goblin):
            goblin.health -= self.power
            print("You do %d damage to the Gobbles." % self.power)
            if goblin.health <= 0:
                print("The Gobbles is dead.")
    # def is_alive(self):
    #     return self.health > 0

    # def health_status(self):
    #     return f'You have {self.health} health and {self.health} power.'