#!/usr/bin/python3
import random
import brain_games.cli
from brain_games.scripts.brain import solver, wrong_answer


def correct(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    return str(num1 + num2)


def main():
    brain_games.cli.welcome_user()
    print('Find the greatest common divisor of given numbers.')
    counter = 0
    THREE_TIMES = 3
    while counter < THREE_TIMES:
        counter += 1
        n1 = random.randint(1, 100)
        n2 = random.randint(1, 50)
        if solver(f'{n1} {n2}', correct(n1, n2)) == 'Correct!':
            print('Correct!')
        else:
            return wrong_answer()

    print(f'Congratulations, {brain_games.cli.name}!')


if __name__ == '__main__':
    main()
