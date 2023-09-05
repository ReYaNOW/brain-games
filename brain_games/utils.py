import random


def get_random_int() -> int:
    return random.randint(1, 100)


def random_choice(iterable: list) -> object:
    return random.choice(iterable)
