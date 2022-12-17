#!/usr/bin/ env python3

from random import randint, choice


GAME = "What is the result of the expression?"


def brain_ring():
    for _ in range(3):
        num1 = randint(1, 50)
        num2 = randint(1, 50)
        operator = choice('+-*')
        question = f"{num1} {operator} {num2}"
        if operator == '+':
            correct_answer = str(num1 + num2)
        elif operator == '-':
            correct_answer = str(num1 - num2)
        else:
            correct_answer = str(num1 * num2)
    return question, correct_answer
