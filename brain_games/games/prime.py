#!/usr/bin/env python3


from random import randint


GAME = 'Answer "yes" if given number is prime. Otherwisr answer "no".'


MIN_NUM = 1
MAX_NUM = 50


def brain_ring():
    num = randint(MIN_NUM, MAX_NUM)
    question = str(num)
    i = 0
    for n in range(2, num // 2 + 1):
        if num % n == 0:
            i += 1
    if i > 0:
        correct_answer = 'no'
    else:
        correct_answer = 'yes'
    return question, correct_answer
