#!/usr/bin/ env python3

from random import randint, choice


GAME = "What is the result of the expression?"


MIIN_NUM = 1
MAX_NUM = 50


def brain_ring():
    num1 = randint(MIIN_NUM, MAX_NUM)
    num2 = randint(MIIN_NUM, MAX_NUM)
    operator = choice('+-*')
    question = f"{num1} {operator} {num2}"
    if operator == '+':
        correct_answer = str(num1 + num2)
    elif operator == '-':
        correct_answer = str(num1 - num2)
    else:
        correct_answer = str(num1 * num2)
    return question, correct_answer
