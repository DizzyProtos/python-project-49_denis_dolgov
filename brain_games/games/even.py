#!/usr/bin/env python3

from random import randint


GAME = 'Answer "yes" if the number is even, otherwise answer "no".'


def brain_ring():
    num = randint(1, 50)
    question = str(num)
    if num % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
