#!/usr/bin/python3


class Enemy:
    def __init__(self, level):
        self.health = 50+(level*5)
        self.attack = 3+(level*2)


class Invader(Enemy):
    def __init__(self, level):
        super().__init__(level)
        self.health += 5
        self.attack += 4

