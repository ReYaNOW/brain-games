import prompt
import brain_games.cli


def wrong_answer(user_answ, correct):
    print(f'"{user_answ}" is wrong answer ;(. Correct answer was "{correct}"')
    return print(f"Let's try again, {brain_games.cli.name}!")


def solver(question, correct_answer):
    correct = correct_answer
    user_answ = prompt.string(f'Question: {question} \nYour answer: ')
    if user_answ == correct:
        return 'Correct!'
    else:
        return wrong_answer(user_answ, correct)
