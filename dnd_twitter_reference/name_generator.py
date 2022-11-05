import random


def generator():
    with open("btn_givennames.txt", encoding='utf8') as file:
        all_text = file.read()
        first_names = list(map(str, all_text.split(f'\n')))
    with open("btn_surnames.txt", encoding='utf8') as file:
        all_text = file.read()
        last_names = list(map(str, all_text.split(f'\n')))
    first = random.choice(first_names)
    last = random.choice(last_names)
    return (f'{first.strip()} {last.strip()}')