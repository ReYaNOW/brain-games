import math

from brain_games.consts import gcd_desc
from brain_games.engine import questioner
from brain_games.utils import get_random_int


def gcd_question():
    num1 = get_random_int()
    num2 = get_random_int(end=50)

    question = f"{num1} {num2}"
    answer = math.gcd(num1, num2)
    return question, answer


def gcd_game():
    questioner(gcd_question, gcd_desc)
