#!/usr/bin/env python3

from random import randint
import prompt


def progression_game():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('What number is missing in the progression?')

    for _ in range(3):
        first_num = randint(1, 20)
        step = randint(1, 5)
        lengt_progression = randint(5, 10)
        last_num = (first_num + step * lengt_progression)
        progression = list(range(first_num, last_num, step))
        index = randint(1, len(progression))
        correct_answer = str(progression[index])
        progression[index] = '..'
        new_progression = " ".join(map(str, progression))
        print(f'Question: {new_progression}')
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct')
        else:
            print('No correct')
    print(f'Congratulations, {name}')
