import math

from brain_games.consts import PRIME_INSTRUCT
from brain_games.engine import ask_questions
from brain_games.utils import get_random_int


def is_prime(number: int) -> bool:
    if number <= 1:
        return False
    for index in range(2, int(math.sqrt(number)) + 1):
        if number % index == 0:
            return False
    return True


def get_prime_num_question():
    num = get_random_int()
    answer = 'yes' if is_prime(num) else 'no'
    return num, answer


def start_prime_num_game():
    ask_questions(get_prime_num_question(), PRIME_INSTRUCT)
