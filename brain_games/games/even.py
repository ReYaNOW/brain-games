#!/usr/bin/python3
import random

from brain_games.scripts.brain import questioner


def check_even(number):
    if number % 2 == 0:
        return "yes"
    else:
        return "no"


def even_game():
    desc = 'Answer "yes" if the number is even, otherwise answer "no".'
    questioner(even_question, desc)


def even_question():
    num = random.randint(1, 100)
    answer = check_even(num)
    return num, answer


if __name__ == "__main__":
    even_game()
