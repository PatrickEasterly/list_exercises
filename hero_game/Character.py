class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
        self.is_alive = True

    def health_power_status(self):
        return f'{self.name} has {self.health} health and {self.power} power. '

    def attack(self, opponent):
        opponent.health -= self.power
        print(f'{self.name} does {self.power} damage to {opponent.name}. ')
    
    def die(self):
        if self.health <= 0:
            self.is_alive = False
            print(f'\n{self.name} is dead!')