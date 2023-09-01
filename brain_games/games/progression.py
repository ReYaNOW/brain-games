from brain_games.consts import progression_desc
from brain_games.engine import questioner
from brain_games.utils import get_random_int


def get_random_progression():
    begin = get_random_int(1, 10)
    end = get_random_int(80, 110)
    step = get_random_int(2, 10)

    result = []
    for i in range(begin, end, step):
        result.append(i)

    max_len = 12
    result = result[:max_len]
    result.sort()

    random_index = get_random_int(1, len(result) - 1)
    correct = result[random_index]
    result[random_index] = ".."
    result = " ".join(map(str, result))
    return result, correct


def progression_game():
    questioner(get_random_progression, progression_desc)
