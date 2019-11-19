class Character:
    def is_alive(self):
        return self.health > 0

    def health_status(self):
        if self.type == 'Hero':
            print('hero message')
        if self.type == 'Goblin':
            print('goblin message')