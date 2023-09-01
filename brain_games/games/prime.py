import math

from brain_games.consts import prime_desc
from brain_games.engine import questioner
from brain_games.utils import get_random_int


def is_prime(number: int) -> bool:
    if number <= 1:
        return False
    for index in range(2, int(math.sqrt(number)) + 1):
        if number % index == 0:
            return False
    return True


def prime_question():
    num = get_random_int()
    answer = "yes" if is_prime(num) else "no"
    return num, answer


def prime_game():
    questioner(prime_question, prime_desc)
