from random import choice
from math import ceil

DEFAULT_OPTIONS = ('rock', 'paper', 'scissors')


def check_options(user_option, comp):
    global score

    if user_option == '!exit':
        print('Bye!')
        return False

    if user_option == '!rating':
        print('Your rating:', score)
    elif user_option not in options:
        print('Invalid input')
    elif user_option == comp:
        score += 50
        print(f'There is a draw ({comp})')
    elif user_option in beats[comp]:
        print(f'Sorry, but the computer chose {comp}')
    else:
        score += 100
        print(f'Well done. The computer chose {comp} and failed')

    return True


def load_score(name):
    file = open('rating.txt')

    u_score = 0
    for line in file:
        f_name, f_score = line.split()
        if f_name == name:
            u_score = int(f_score)

    file.close()

    return u_score


def get_options():
    text = input()
    return tuple(text.split(',')) if text else DEFAULT_OPTIONS


def build_beats(data):
    all_beats = {}
    for pos, option in enumerate(data):
        other_options = data[pos + 1:] + data[:pos]
        all_beats[option] = other_options[ceil(len(other_options) / 2):]

    return all_beats


def get_username():
    name = input('Enter your name: ')
    print(f'Hello, {name}')
    return name


username = get_username()
options = get_options()
beats = build_beats(options)
score = load_score(username)

print("Okay, let's start")
while check_options(input(), choice(options)):
    pass
