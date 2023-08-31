import random

import prompt


def welcome_user(desc=""):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")

    if desc:
        print(desc)
    return name


def get_random_int(begin=1, end=100):
    return random.randint(begin, end)
