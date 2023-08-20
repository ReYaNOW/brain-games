#!/usr/bin/python3
import random

from brain_games.scripts.brain import questioner


def calculate_answer(a: int, b: int, operator: str):
    match operator:
        case "+":
            return str(a + b)
        case "-":
            return str(a - b)
        case "*":
            return str(a * b)


def calc_game():
    desc = "What is the result of the expression?"
    questioner(calc_question, desc)


def calc_question():
    symbols = ["+", "-", "*"]
    symbol = random.choice(symbols)

    num1 = random.randint(1, 100)
    num2 = random.randint(1, 15)

    question = f"{num1} {symbol} {num2}"
    answer = calculate_answer(num1, num2, symbol)
    return question, answer


if __name__ == "__main__":
    calc_game()
