#!/usr/bin/python3
import math
import random

import brain_games.cli
from brain_games.scripts.brain import solver


def find_answer(num1, num2):
    gcd = math.gcd(num1, num2)
    return str(gcd)


def main():
    name = brain_games.cli.welcome_user()
    print("Find the greatest common divisor of given numbers.")

    counter = 0
    three_times = 3

    while counter < three_times:
        counter += 1
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 50)

        answer = find_answer(num1, num2)
        user_answer = solver(f"{num1} {num2}", answer, name)
        if user_answer == "incorrect":
            return

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
