#!/usr/bin/env python3

from random import randint


GAME = 'What number is missing in the progression?'


def brain_ring():
    first_num = randint(1, 20)
    step = randint(1, 5)
    lengt_progression = randint(5, 10)
    last_num = (first_num + step * lengt_progression)
    progression = list(range(first_num, last_num, step))
    index = randint(1, len(progression))
    correct_answer = str(progression[index])
    progression[index] = '..'
    question = " ".join(map(str, progression))
    return question, correct_answer
