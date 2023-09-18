from brain_games.consts import EVEN_INSTRUCT
from brain_games.engine import run_game
from brain_games.utils import get_random_int


def is_even(number):
    return number % 2 == 0


def get_even_expression_and_answer() -> tuple[int, str]:
    number = get_random_int()
    answer = 'yes' if is_even(number) else 'no'
    return number, str(answer)


def start_even_game():
    run_game(get_even_expression_and_answer, EVEN_INSTRUCT)
