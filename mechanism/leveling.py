#!/usr/bin/python3


def levelup(player):
    if player.name == 'Warrior':
        player.attack += 8
        player.level += 1
    elif player.name == 'Solider':
        player.attack += 5
        player.level += 1
    elif player.name == 'Potent':
        player.attack += 11
        player.level += 1
    return player.level
