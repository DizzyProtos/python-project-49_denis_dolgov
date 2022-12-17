#!/usr/bin/env python3


from random import randint


GAME = 'Answer "yes" if given number is prime. Otherwisr answer "no".'


def brain_ring():
    num = randint(1, 100)
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
