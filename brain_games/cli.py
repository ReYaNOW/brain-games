import prompt


def welcome_user(game_instruction=''):
    name = prompt.string("Welcome to the Brain Games!\nMay I have your name? ")
    print(f"Hello, {name}!{game_instruction}")
