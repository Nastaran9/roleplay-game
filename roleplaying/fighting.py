#!/usr/bin/python3


from random import randint
from random import uniform
import time


def fight(player, enemy):
    go = True
    while go is True :
        variance = player.attack * 0.5
        Evariance = enemy.attack * 0.2
        dmg = uniform(player.attack - variance, player.attack + variance)
        Edmg = uniform(enemy.attack - Evariance, enemy.attack + Evariance)
        print('dmg= {} *** dmg = {}'.format(dmg,Edmg))
        enemy.health -= dmg
        mis = randint(1, 100)
        if mis <= 5:
            player.health = player.health
        player.health -= Edmg
        print('player.health=%d *** enemy.health=%d'%(player.health, enemy.health))
        if player.health <= 0:
            print('You have been slain by the enemy')
            go = False
            time.sleep(3)
        elif enemy.health <= 0:
            print('You have slain the enemy')
            player.ex += 50
            if player.ex >= 100:
                player.level += 1
                player.attack += 8
                player.ex -= 100
            go = False
            time.sleep(3)


if __name__ == '__main__':
    fight(player, enemy)
