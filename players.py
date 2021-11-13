#!/usr/bin/python3

class Human:
    def __init__(self):
        self.health = 100
        self.attack = 10
        self.level = 1
        self.ex = 0


class Warrior(Human):
    def __init__(self):
        super().__init__()
        self.health += 15
        self.attack += 3
        self.name = 'Warrior'


class Solider(Human):
    def __init__(self):
        super().__init__()
        self.health += 10
        self.attack -= 3
        self.name = 'Solider'


class Potent(Human):
    def __init__(self):
        super().__init__()
        self.health += 20
        self.attack += 2
        self.name = 'Potent'
