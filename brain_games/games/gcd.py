import math

from brain_games.consts import GCD_INSTRUCT
from brain_games.engine import run_game
from brain_games.utils import get_random_int


def get_gcd_expression_and_answer():
    num1, num2 = get_random_int(), get_random_int()

    question = f'{num1} {num2}'
    answer = math.gcd(num1, num2)
    return question, str(answer)


def start_gcd_game():
    run_game(get_gcd_expression_and_answer, GCD_INSTRUCT)
