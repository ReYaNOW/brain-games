import math

from brain_games.engine import questioner, get_random_int


def get_gcd(num1, num2):
    gcd = math.gcd(num1, num2)
    return str(gcd)


def gcd_game():
    desc = "Find the greatest common divisor of given numbers."
    questioner(gcd_question, desc)


def gcd_question():
    num1 = get_random_int()
    num2 = get_random_int(end=50)

    question = f"{num1} {num2}"
    answer = get_gcd(num1, num2)

    return question, answer
