from brain_games.consts import PRIME_INSTRUCT
from brain_games.engine import run_game
from brain_games.utils import get_random_int


def is_prime(number: int) -> bool:
    if number <= 1:
        return False
    for index in range(2, number ** 2 + 1):
        if number % index == 0:
            return False
    return True


def get_prime_num_expression_and_answer() -> tuple[int, str]:
    num = get_random_int()
    answer = 'yes' if is_prime(num) else 'no'
    return num, answer


def start_prime_num_game():
    run_game(get_prime_num_expression_and_answer, PRIME_INSTRUCT)
