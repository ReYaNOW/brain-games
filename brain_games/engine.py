import prompt

from brain_games.consts import three_times


def questioner(get_quest_and_answer: callable, game_instruction: str):
    name = prompt.string("Welcome to the Brain Games!\nMay I have your name?")
    print(f"Hello, {name}!{game_instruction}")

    message = "is wrong answer ;(. Correct answer was"

    for _ in range(three_times):
        question, correct_answer = get_quest_and_answer()
        user_answer = prompt.string(f"Question: {question} \nYour answer: ")

        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' {message} '{correct_answer}'")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
