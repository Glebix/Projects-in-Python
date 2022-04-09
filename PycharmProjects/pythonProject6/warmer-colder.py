from random import shuffle

TRIES = 10
MAX_DIGITS = 3
guesses_taken = 1


def random_num():
    list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    shuffle(list_of_numbers)
    secret_num = ""
    for i in range(MAX_DIGITS):
        secret_num += str(list_of_numbers[i])
    return secret_num


def get_clues(guess, secret_num):
    global clues
    clues = []
    for i in range(len(guess)):
        if guess[i] in secret_num and guess[i] != secret_num[i]:
            clues.append("Warmer")
        elif guess[i] == secret_num[i]:
            clues.append("Hotter")
        else:
            clues.append("__")
    if len(clues) == 0:
        return "Cold"
    return " ".join(clues)


def is_digit():
    while True:
        guess = input("enter a number: ")
        if len(guess) > 3 or len(guess) < 3:
            print("Enter a three digit number: ")
        elif not guess.isdigit():
            print("Enter a correct number: ")
        elif guess == ' ':
            print("Enter a correct number")
        else:
            return guess


print("""
    You will be given a three digit number that you must guess
    I'll give you some hints
    Cold:Not a single figure was guessed.
    Heat:One digit is guessed, but its position is not guessed.
    Hot:One digit and its position are guessed.


    """)
secret_number = random_num()
while True:
    guess = is_digit()
    if guess == secret_number:
        print("You've won")
        ans = input("Play again(y/yes): ")
        if not ans.lower().startswith('y'):
            guesses_taken = 1

            break
        else:
            guesses_taken = 1
            secret_number = random_num()
            continue
    else:
        print(get_clues(guess, secret_number))
        clues = []
        guesses_taken += 1
    if guesses_taken > TRIES:
        print(f"Out of tries number was {secret_number}")
