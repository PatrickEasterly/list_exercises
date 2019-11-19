from Character import Character
class Goblin(Character):
    def __init__(self, name):
        super().__init__(name, 6, 2)



    # def __init__(self):
    #     self.health = 6
    #     self.power = 2
    #     self.type = 'Goblin'
    # def attack(self, hero):
    #         hero.health -= self.power
    #         print("The Goblin does %d damage to you." % self.power)
    #         if hero.health <= 0:
    #             print("The Gobbles is dead.")
    # def is_alive(self):
    #     return self.health > 0

    # def health_status(self):
    #     return f'The goblin has {self.health} health and {self.power} power.'
