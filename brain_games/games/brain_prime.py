#!/usr/bin/python3
import random
import brain_games.cli
from brain_games.scripts.brain import solver, wrong_answer


def correct(number):
    if number == 1:
        return 'no'
    result = 2
    while result < number / 2:
        if number % result == 0:
            return 'no'
        result += 1
    return 'yes'


def main():
    brain_games.cli.welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
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
