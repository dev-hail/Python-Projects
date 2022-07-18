import random
import sys


def guess_game(x):
    guess = 0
    random_number = random.randint(1, x)

    while guess != random_number:
        try:
            guess = int(input(f'Guess a number between 1 - {x} :'))
            if guess < random_number:
                print('It\'s too low')
            elif guess > random_number:
                print("its too high!")
            elif guess == random_number:
                print("you guessed correctly! congrats!")
        except:
            print('pls input a number!')
guess_game(10)