#!/usr/bin/python3
import random
import brain_games.cli
from brain_games.scripts.brain import solver, wrong_answer


def correct(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def main():
    brain_games.cli.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    counter = 0
    THREE_TIMES = 3
    while counter < THREE_TIMES:
        counter += 1
        num = random.randint(1, 100)
        if solver(f'{num}', correct(num)) == 'Correct!':
            print('Correct!')
        else:
            return wrong_answer()
    print(f'Congratulations, {brain_games.cli.name}!')


if __name__ == '__main__':
    main()
