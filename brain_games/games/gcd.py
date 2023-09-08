import math

from brain_games.consts import GCD_INSTRUCT
from brain_games.engine import ask_questions
from brain_games.utils import get_random_int


def get_gcd_question():
    num1 = get_random_int()
    num2 = get_random_int()

    question = f'{num1} {num2}'
    answer = math.gcd(num1, num2)
    return question, str(answer)


def start_gcd_game():
    ask_questions(get_gcd_question, GCD_INSTRUCT)
