#!/usr/bin/env pyrhon3


from random import randint
import math


GAME = 'Find the greatwst common divisor of given numbers'


def brain_ring():
    num1 = randint(1, 50)
    num2 = randint(1, 50)
    question = f'{num1} and {num2}'
    correct_answer = str(math.gcd(num1, num2))
    return question, correct_answer
