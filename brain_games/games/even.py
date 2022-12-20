#!/usr/bin/env python3

from random import randint


GAME = 'Answer "yes" if the number is even, otherwise answer "no".'


MIN_NUM = 1
MAX_NUM = 50


def brain_ring():
    num = randint(MIN_NUM, MAX_NUM)
    question = str(num)
    if num % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
