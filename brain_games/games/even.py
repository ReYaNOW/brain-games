from brain_games.engine import questioner
from brain_games.utils import get_random_int


def check_even(number):
    if number % 2 == 0:
        return "yes"
    else:
        return "no"


def even_game():
    desc = 'Answer "yes" if the number is even, otherwise answer "no".'
    questioner(even_question, desc)


def even_question():
    num = get_random_int()
    answer = check_even(num)
    return num, answer
