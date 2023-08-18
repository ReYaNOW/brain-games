import prompt


def solver(question, correct_answer, name):
    user_answer = prompt.string(f"Question: {question} \nYour answer: ")
    if user_answer == correct_answer:
        print("Correct!")
    else:
        wrong_answer(user_answer, correct_answer, name)
        return 'incorrect'


def wrong_answer(user_answer, answer, name):
    print(
        f'"{user_answer}" is wrong answer ;(. Correct answer was "{answer}"'
    )
    return print(f"Let's try again, {name}!")
