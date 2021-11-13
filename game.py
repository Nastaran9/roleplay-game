#!/usr/bin/python3


from random import randint
from random import uniform
import players
import enemys
from mechanism import fighting
from mechanism import leveling

import time


def get_player():
    selection = int(input('which class do you want to be?\n1.warrior\n2.solider\n3.potent\nEnter a value:'))
    if selection == 1:
        player = players.Warrior()
    elif selection == 2:
        player = players.Solider()
    elif selection == 3:
        player = players.Potent()
    return player


def game_loop(player):
    while True:
        print('Do you want to play or Exit?')
        time.sleep(0.5)
        print('1.play\n2.Exit')
        play = int(input('Enter a value: '))
        
        
        if play == 1:
            enemy = enemys.Invader(player.level)
            fighting.fight(player, enemy)
            print('The level of enemy is {}'.format(player.level))
        elif play == 2:
            print('..........................Bye,Have a nice time..........................')
            break



def main():
    player = get_player()
    game_loop(player)


if __name__ == '__main__':
    main()
