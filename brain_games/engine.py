import prompt

from brain_games.consts import AMOUNT_OF_ROUNDS


def ask_questions(get_quest_and_answer: callable, game_instruction: str):
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')
    print(f'Hello, {name}!\n{game_instruction}')

    for _ in range(AMOUNT_OF_ROUNDS):
        question, correct_answer = get_quest_and_answer()
        user_answer = prompt.string(f'Question: {question} \nYour answer: ')

        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(
                f'\'{user_answer}\' is wrong answer ;(. Correct answer was\
            \'{correct_answer}\'\nLet\'s try again, {name}!'
            )
            return

    print(f'Congratulations, {name}!')
