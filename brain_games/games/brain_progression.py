#!/usr/bin/python3
import random
import brain_games.cli
from brain_games.scripts.brain import solver, wrong_answer


def rnd_prgrs():
    begin = random.randint(1, 10)
    end = random.randint(80, 110)
    n = random.randint(2, 10)
    result = []
    for i in range(begin, end, n):
        result.append(i)
    result = result[:12]
    result.sort()
    random_index = random.randint(1, len(result) - 1)
    correct = str(result[random_index])
    result[random_index] = '..'
    result = ' '.join(map(str, result))
    return result, correct


def main():
    brain_games.cli.welcome_user()
    print('What number is missing in the progression?')
    counter = 0
    THREE_TIMES = 3
    while counter < THREE_TIMES:
        counter += 1
        if solver(*rnd_prgrs()) == 'Correct!':
            print('Correct!')
        else:
            return wrong_answer()

    print(f'Congratulations, {brain_games.cli.name}!')


if __name__ == '__main__':
    main()
