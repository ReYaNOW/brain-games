import math
import random

from brain_games.engine import questioner


def get_gcd(num1, num2):
    gcd = math.gcd(num1, num2)
    return str(gcd)


def gcd_game():
    desc = "Find the greatest common divisor of given numbers."
    questioner(gcd_question, desc)


def gcd_question():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 50)

    question = f"{num1} {num2}"
    answer = get_gcd(num1, num2)

    return question, answer


if __name__ == "__main__":
    gcd_game()
