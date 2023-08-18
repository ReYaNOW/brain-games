#!/usr/bin/python3
import random

import brain_games.cli
from brain_games.scripts.brain import solver


def find_answer(number):
    if number % 2 == 0:
        return "yes"
    else:
        return "no"


def main():
    name = brain_games.cli.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    counter = 0
    three_times = 3

    while counter < three_times:
        counter += 1
        num = random.randint(1, 100)

        answer = find_answer(num)
        user_answer = solver(f"{num}", answer, name)
        if user_answer == "incorrect":
            return

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
