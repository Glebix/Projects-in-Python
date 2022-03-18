import random

HANGMAN_PICS = ['''
       +---+
           |
           |
           |
          ===''', '''
       +---+
       O   |
           |
           |
          ===''', '''
       +---+
       O   |
       |   |
           |
          ===''', '''
       +---+
       O   |
      /|   |
           |
          ===''', '''
       +---+
       O   |
      /|\  |
           |
          ===''', '''
       +---+
       O   |
      /|\  |
      /    |
          ===''', '''
      LAST CHANCE
       +---+
       O   |
      /|\  |
      / \  |
          ===''']

word_list = """bite python mouse fool equipment google duck line wind cozy aqua moon doom broom bread nonsense good god boom fort hello string giraffe cat pet pal mall pine fine wine lime leak pick tool pool game fame lame time hire fire float soccer poker joker kilogram binary finally sense yummy tire liar play say blame can janitor ton bone coin wife guide quite pain honest reliable claim book look""".split(
    ' ')


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w',
            'x', 'y', 'z']



def get_guess(guess):
    flag = True
    while flag:
        if len(guess) > 1:
            print("Enter a letter not a string")
            guess = input()
        elif guess.lower() not in alphabet:
            print('Enter an English letter')
            guess = input()
        elif guess in missed_words:
            print('You have already tried this letter')
            guess = input()
        elif guess in word_to_guess:
            print("You've already guessed it")
            guess = input()
        else:
            return guess


def game():
    random_word = random.choice(word_list)
    global guess, missed_words,word_to_guess,missed_words
    missed_words = []
    word_to_guess = len(random_word) * '_'
    print("Welcome to Hangman")
    while True:
        guess = get_guess(input('Enter a guess: '))
        if guess not in random_word:
            missed_words.append(guess)
            if len(missed_words) > len(HANGMAN_PICS):
                print('GAME OVER')
                ans = input(f"You've lost.The word was {random_word}.Do you wanna play again(Yes/y)").lower()
                if ans == 'y' or ans == 'yes':
                    random_word = random.choice(word_list)
                    word_to_guess = len(random_word) * '_'
                    game()
                    missed_words = []
                else:
                    return 'Bye'
            else:
                print("Incorrect")
                print(HANGMAN_PICS[len(missed_words) - 1])
        else:
            for i in range(len(random_word)):
                if guess == random_word[i]:
                    word_to_guess = word_to_guess[:i] + guess + word_to_guess[i + 1:]
                    print(word_to_guess)
            if word_to_guess == random_word:
                ans = input("You've won! Do you wanna play again(Yes/y)").lower()
                if ans == 'y' or ans == 'yes':
                    random_word = random.choice(word_list)
                    word_to_guess = len(random_word) * '_'
                    game()
                    missed_words = []
                else:
                    return "Bye"


print(game())
