#!/usr/bin/python3


from random import randint
from random import uniform
from roleplaying.opponent import players
from roleplaying.foe import enemys
from roleplaying import fighting
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
        enemy = enemys.Invader(player.level)
        print('The level of enemy is %d.\nDo you want to play or Exit?' % player.level)
        print('1.play\n2.Exit')
        play = int(input('Enter a value: '))
        if play == 1:
            fighting.fight(player, enemy)
        elif play == 2:
            print('Bye')
            break


def main():
    player = get_player()
    game_loop(player)


if __name__ == '__main__':
    main()
