from brain_games.engine import questioner
from brain_games.utils import get_random_int


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
    index = get_random_int(0, 2)
    symbol = symbols[index]

    num1 = get_random_int()
    num2 = get_random_int(end=15)

    question = f"{num1} {symbol} {num2}"
    answer = calculate_answer(num1, num2, symbol)
    return question, answer
