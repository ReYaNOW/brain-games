import random


def get_random_int(begin: int = 1, end: int = 100) -> int:
    return random.randint(begin, end)


def random_choice(iterable: list) -> object:
    return random.choice(iterable)
