import math

from brain_games.consts import GCD_DESC
from brain_games.engine import questioner
from brain_games.utils import get_random_int


def gcd_question():
    num1 = get_random_int()
    num2 = get_random_int()

    question = f"{num1} {num2}"
    answer = math.gcd(num1, num2)
    return question, answer


def gcd_game():
    questioner(gcd_question, GCD_DESC)
