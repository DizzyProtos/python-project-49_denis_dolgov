from random import randint
import prompt


def welcome_and_start(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')


def is_even():
    round = 3
    for _ in range(round):
        x = randint(1, 50)
        if x % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        print(f'Question: {x}')
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"{answer} is wrong answer ;(."
                  f"Correct answer was {correct_answer}"
                  f"Let\'s try again, {name}!")
        break
    print(f'Congratulations, {name}!')
