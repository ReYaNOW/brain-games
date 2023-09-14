from random import randint

from brain_games.consts import PROGRESSION_INSTRUCT, PROGRESSION_LEN
from brain_games.engine import run_game
from brain_games.utils import get_random_int


def get_progression_and_missed_number():
    begin = get_random_int()
    step = get_random_int()
    missed_num_ind = randint(0, PROGRESSION_LEN - 1)

    progression = [
        '..' if i == missed_num_ind else str(begin + i * step)
        for i in range(PROGRESSION_LEN)
    ]

    str_progression = ' '.join(progression)
    missed_num = begin + missed_num_ind * step
    return str_progression, str(missed_num)


def start_progression_game():
    run_game(get_progression_and_missed_number, PROGRESSION_INSTRUCT)
