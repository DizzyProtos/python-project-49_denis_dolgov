from random import randint


GAME_EVEN = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even():
    x = randint(1,100) #выводится случайное число
    if x % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return str(x), answer
