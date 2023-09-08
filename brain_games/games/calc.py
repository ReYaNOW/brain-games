from brain_games.consts import CALC_INSTRUCT
from brain_games.engine import ask_questions
from brain_games.utils import get_random_int, random_choice


def get_calc_question():
    num1 = get_random_int()
    num2 = get_random_int()

    symbols = ['+', '-', '*']
    symbol = random_choice(symbols)

    match symbol:
        case '+':
            answer = num1 + num2
        case '-':
            answer = num1 - num2
        case _:
            answer = num1 * num2

    question = f'{num1} {symbol} {num2}'
    return question, str(answer)


def start_calc_game():
    ask_questions(get_calc_question, CALC_INSTRUCT)
