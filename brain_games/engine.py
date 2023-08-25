#!/usr/bin/python3
import prompt


def questioner(get_quest_and_answer, desc):
    name = welcome_user(desc)

    counter = 0
    three_times = 3

    while counter < three_times:
        counter += 1

        question, correct_answer = get_quest_and_answer()
        user_answer = prompt.string(f"Question: {question} \nYour answer: ")

        if user_answer == correct_answer:
            print("Correct!")
        else:
            wrong_answer(user_answer, correct_answer, name)
            return "incorrect"

    print(f"Congratulations, {name}!")


def wrong_answer(user_answer, answer, name):
    print(f'"{user_answer}" is wrong answer ;(. Correct answer was "{answer}"')
    return print(f"Let's try again, {name}!")


def welcome_user(desc=""):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")

    if desc:
        print(desc)
    return name


def main():
    welcome_user()


if __name__ == "__main__":
    main()
