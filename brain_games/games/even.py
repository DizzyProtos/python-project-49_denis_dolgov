#!/usr/bin/env python3

from random import randint
import prompt


def even_game():
    print('Welcome to the Braine Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('Answer "yes" if the number is even, otherwise answer "no".')

    for _ in range(3):
        num = randint(1, 50)
        if num % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        print(f'Question:, {num}')
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct')
        else:
            print(f"'{answer}' is wrong answer ;(."
                  f"Correct answer was '{correct_answer}'."
                  f"Let's try again, {name}!")
    print(f'Congratulations, {name}!')
