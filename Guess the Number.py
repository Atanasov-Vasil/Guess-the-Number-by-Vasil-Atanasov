import random
from colorama import Fore


def game(some_integer, some_number):
    if 100 > some_integer > 0:
        if some_integer == some_number:
            print(Fore.GREEN + f'Great! You guessed the number in {count} attempts!')
            print('Bye, bye!')
            is_correct = True
            return is_correct
        elif some_integer > some_number:
            print(Fore.RED + f'You aim too high')
        else:
            print(Fore.YELLOW + f'You aim too low')


print(Fore.BLUE + 'This is a game of "Guess the Number"!')

number = random.randint(1, 100)

count = 0

is_correct = False
while not is_correct:
    guess = input((Fore.RESET + 'Please, enter a number between 1 and 100!'))
    if guess.isdigit():
        guess = int(guess)
        is_correct = game(guess, number)
        count += 1
    else:
        guess = input((Fore.RESET + 'Invalid input! Please, enter a NUMBER between 1 and 100!'))
else:
    exit()
