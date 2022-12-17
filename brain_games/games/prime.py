#!/usr/bin/env python3


from random import randint


GAME = 'Answer "yes" if given number is prime. Otherwisr answer "no".'


def brain_ring():
    num = randint(1, 100)
    i = 0
    k = 1
    question = str(num)
    while k <= num:
        if num % k == 0:
            i += 1
            k += 1
        if i == 2:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
    return question, correct_answer
