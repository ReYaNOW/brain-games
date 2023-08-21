#!/usr/bin/python3
import random

from brain_games.scripts.brain import questioner


def get_random_progression():
    begin = random.randint(1, 10)
    end = random.randint(80, 110)
    step = random.randint(2, 10)

    result = []
    for i in range(begin, end, step):
        result.append(i)

    max_len = 12
    result = result[:max_len]
    result.sort()

    random_index = random.randint(1, len(result) - 1)
    correct = str(result[random_index])
    result[random_index] = ".."
    result = " ".join(map(str, result))
    return result, correct


def progression_game():
    desc = "What number is missing in the progression?"
    questioner(progression_question, desc)


def progression_question():
    progression, answer = get_random_progression()
    return progression, answer


if __name__ == "__main__":
    progression_game()
