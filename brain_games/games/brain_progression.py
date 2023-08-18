#!/usr/bin/python3
import random
import brain_games.cli
from brain_games.scripts.brain import solver


def random_progression():
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


def main():
    name = brain_games.cli.welcome_user()
    print("What number is missing in the progression?")
    counter = 0
    three_times = 3
    while counter < three_times:
        counter += 1

        progression, answer = random_progression()
        user_answer = solver(progression, answer, name)
        if user_answer == "incorrect":
            return

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
