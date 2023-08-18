#!/usr/bin/python3
import random

import brain_games.cli
from brain_games.scripts.brain import solver


def find_answer(a: int, b: int, operator: str):
    match operator:
        case "+":
            return str(a + b)
        case "-":
            return str(a - b)
        case "*":
            return str(a * b)


def main():
    name = brain_games.cli.welcome_user()
    print("What is the result of the expression?")

    symbols = ["+", "-", "*"]
    counter = 0
    three_times = 3

    while counter < three_times:
        counter += 1
        symbol = random.choice(symbols)
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 15)

        answer = find_answer(num1, num2, symbol)
        user_answer = solver(f"{num1} {symbol} {num2}", answer, name)
        if user_answer == "incorrect":
            return

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
