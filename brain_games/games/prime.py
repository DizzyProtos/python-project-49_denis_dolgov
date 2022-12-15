#!/usr/bin/env python3


from random import randint
import prompt


def prime_game():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have yor name? ')
    print(f'Hello, {name}')
    print('Answer "yes" if given number is prime. Otherwisr answer "no".')

    for _ in range(3):
        num = randint(1, 100)
        i = 0
        k = 1
        while k <= num:
            if num % k == 0:
                i += 1
            k += 1
        if i == 2:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        print(f'Question: {num}')
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct')
        else:
            print('No correct')
    print(f'Confiratulation, {name}')
