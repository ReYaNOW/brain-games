import prompt


def welcome_user(desc=""):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    
    if desc:
        print(desc)
    return name
