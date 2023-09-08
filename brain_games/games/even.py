from brain_games.consts import EVEN_INSTRUCT
from brain_games.engine import ask_questions
from brain_games.utils import get_random_int


def get_even_question():
    number = get_random_int()
    answer = 'yes' if number % 2 == 0 else 'no'
    return number, str(answer)


def start_even_game():
    ask_questions(get_even_question, EVEN_INSTRUCT)
