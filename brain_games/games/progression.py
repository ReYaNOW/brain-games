from random import randint

from brain_games.consts import PROGRESSION_DESC, PROGRESSION_LEN
from brain_games.engine import questioner
from brain_games.utils import get_random_int


def get_random_progression():
    begin = get_random_int()
    step = get_random_int()
    missed_num_ind = randint(0, PROGRESSION_LEN - 1)

    progression = [
        ".." if i == missed_num_ind else str(begin + i * step)
        for i in range(PROGRESSION_LEN)
    ]

    str_progression = " ".join(progression)
    missed_num = begin + missed_num_ind * step
    return str_progression, missed_num


def progression_game():
    questioner(get_random_progression, PROGRESSION_DESC)
