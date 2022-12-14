#!/usr/bin/env pyrhon3


from random import randint
import prompt
import math


def gcd_game():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('Find the greatwst common divisor of given numbers')

    for _ in range(3):
        num1 = randint(1, 50)
        num2 = randint(1, 50)
        correct_answer = math.gcd(num1, num2)
        print(f"Question: {num1} and {num2}")
        answer = int(prompt.string('Your answer: '))
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\nLet's try again, {name}!")
    print(f'Confiratulation, {name}!')
