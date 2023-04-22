#!/usr/bin/python3
import random
import brain_games.cli
from brain_games.scripts.brain import solver


def calc(a: int, b: int, operator: str):
    match operator:
        case "+":
            return str(a + b)
        case "-":
            return str(a - b)
        case "*":
            return str(a * b)


def main():
    brain_games.cli.welcome_user()
    print("What is the result of the expression?")
    SYMBOLS = ["+", "-", "*"]
    counter = 0
    THREE_TIMES = 3
    while counter < THREE_TIMES:
        counter += 1
        rn_sy = random.choice(SYMBOLS)
        n1 = random.randint(1, 100)
        n2 = random.randint(1, 15)
        if solver(f"{n1} {rn_sy} {n2}", calc(n1, n2, rn_sy)) == "Correct!":
            print("Correct!")
        else:
            return None

    print(f"Congratulations, {brain_games.cli.name}!")


if __name__ == "__main__":
    main()
