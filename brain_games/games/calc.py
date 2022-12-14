#!/usr/bin/env python3

from random import randint
from random import choice
import prompt


def calc_game():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('What is the result of the expression?')

    for _ in range(3):
        num1 = randint(1, 50)
        num2 = randint(1, 50)
        operator = choice('+-*')
        if operator == '+':
            correct_answer = num1 + num2
        elif operator == '-':
            correct_answer = num1 - num2
        else:
            correct_answer = num1 * num2
        print(f"'Question:' {num1} {operator} {num2}")
        answer = int(prompt.string('Your answer: '))
        if answer == correct_answer:
            print('Correct')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'./nLet's try again, {name}!")
    print(f'Confiratulation, {name}!')
