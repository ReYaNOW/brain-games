from random import randint

from brain_games.consts import PROGRESSION_INSTRUCT, PROGRESSION_LEN
from brain_games.engine import run_game
from brain_games.utils import get_random_int


def generate_progression(begin, step, missed_num_ind):
    return [
        '..' if i == missed_num_ind else str(begin + i * step)
        for i in range(PROGRESSION_LEN)
    ]


def get_progression_and_missed_number() -> tuple[str, str]:
    begin, step = get_random_int(), get_random_int()
    missed_num_ind = randint(0, PROGRESSION_LEN - 1)
    progression = generate_progression(begin, step, missed_num_ind)

    str_progression = ' '.join(progression)
    missed_num = begin + missed_num_ind * step
    return str_progression, str(missed_num)


def start_progression_game():
    run_game(get_progression_and_missed_number, PROGRESSION_INSTRUCT)
