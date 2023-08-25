import math

from brain_games.engine import questioner, get_random_int


def check_prime(number):
    if number <= 1:
        return False
    for index in range(2, int(math.sqrt(number)) + 1):
        if number % index == 0:
            return False
    return True


def prime_game():
    desc = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    questioner(prime_question, desc)


def prime_question():
    num = get_random_int()
    answer = check_prime(num)
    return num, answer
