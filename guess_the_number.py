# guess the number
from random import randint

number = randint(1, 100)


def game():
    hint = input('Do you wanna hint.Yes or No: ')
    if hint.lower().startswith('y'):
        if 1 <= number <= 50:
            print('From 1 to 50')
        elif 51 <= number <= 100:
            print('From 51 to 100')
    tries = 0
    while tries != 10:
        try:
            guess = int(input('Enter the guess: '))
        except ValueError:
            print("enter number not a string")
            continue
        if guess == number:
            print('You won.Number of tries {}'.format(tries))
            choise = input("Do you wanna play again: ")
            if choise == "Yes" or choise == "y":
                game()
            else:
                break
        elif guess < number:
            print("Try Bigger")
            tries += 1
        elif guess > number:
            print("Try smaller")
            tries += 1
        if tries == 10:
            print(f"You've lost the guess was{number}")
            choise = input('Play again: ')
            if choise == "Yes" or choise == "y":
                game()
            else:
                break


game()
