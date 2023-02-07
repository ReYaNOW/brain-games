import prompt
import brain_games.cli


def solver(question, correct_answer):
    global user_answ, correct
    correct = correct_answer
    user_answ = prompt.string(f'Question: {question} \nYour answer: ')
    if user_answ == correct:
        return 'Correct!'


def wrong_answer():
    print(f'"{user_answ}" is wrong answer ;(. Correct answer was "{correct}"')
    return print(f"Let's try again, {brain_games.cli.name}!")
