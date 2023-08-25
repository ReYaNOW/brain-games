import random

from brain_games.engine import questioner


def check_prime(number):
    if number == 1:
        return "no"
    result = 2
    while result < number:
        if number % result == 0:
            return "no"
        result += 1
    return "yes"


def prime_game():
    desc = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    questioner(prime_question, desc)


def prime_question():
    num = random.randint(1, 100)
    answer = check_prime(num)
    return num, answer


if __name__ == "__main__":
    prime_game()
