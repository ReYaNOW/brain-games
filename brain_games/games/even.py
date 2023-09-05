from brain_games.consts import EVEN_DESC
from brain_games.engine import questioner
from brain_games.utils import get_random_int


def is_even(number: int) -> bool:
    if number % 2 == 0:
        return True
    return False


def even_question():
    num = get_random_int()
    answer = "yes" if is_even(num) else "no"
    return str(num), answer


def even_game():
    questioner(even_question, EVEN_DESC)
