from random import choice

from brain_games.consts import CALC_INSTRUCT
from brain_games.engine import run_game
from brain_games.utils import get_random_int


def get_calc_expression_and_answer() -> tuple[str, str]:
    num1, num2 = get_random_int(), get_random_int()

    symbols = ['+', '-', '*']
    symbol = choice(symbols)

    match symbol:
        case '+':
            answer = num1 + num2
        case '-':
            answer = num1 - num2
        case _:
            answer = num1 * num2

    question = f'{num1} {symbol} {num2}'
    return question, str(answer)


def start_calc_game():
    run_game(get_calc_expression_and_answer, CALC_INSTRUCT)
