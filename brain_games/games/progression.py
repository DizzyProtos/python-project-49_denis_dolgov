#!/usr/bin/env python3

from random import randint


GAME = 'What number is missing in the progression?'


def brain_ring():
    first_num = randint(1, 20)
    step = randint(1, 5)
    lengt_progression = randint(5, 10)
    progression = [first_num]
    while len(progression) < lengt_progression:
        progression.append(progression[-1] + step)
    index = randint(0, len(progression) - 1)
    correct_answer = str(progression[index])
    progression[index] = '..'
    question = " ".join(map(str, progression))
    return question, correct_answer
