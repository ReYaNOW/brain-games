from operator import add, sub, mul

from brain_games.consts import calc_desc
from brain_games.engine import questioner
from brain_games.utils import get_random_int, random_choice


def calc_question():
    operations = [("+", add), ("-", sub), ("*", mul)]
    symbol, operation = random_choice(operations)

    num1 = get_random_int()
    num2 = get_random_int(end=15)

    question = f"{num1} {symbol} {num2}"
    answer = operation(num1, num2, operation)
    return question, answer


def calc_game():
    questioner(calc_question, calc_desc)
