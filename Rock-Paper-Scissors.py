from random import choice

ans = ['rock', 'paper', 'scissors']


def game():
    while True:
        print('Welcome to Rock Paper Scissors')
        try:
            player_move = input('Choose Rock,Paper or Scissors: ')
            if player_move.lower() not in ans:
                player_move = input('Choose Rock Paper or Scissors: ')
        except ValueError:
            player_move = input('Choose Rock,Paper or Scissors: ')
        computer_move = choice(ans)
        if computer_move == player_move:
            print('Tie')
            play_again = input('Do you wanna play again: ')
            if play_again.lower() == 'yes' or play_again.lower() == 'y':
                game()
            else:
                quit()
        elif (computer_move == 'rock' and player_move.lower() == 'scissors') or (
                computer_move == 'scissors' and player_move.lower() == 'paper') or (
                computer_move == 'paper' and player_move.lower() == 'rock'):
            print('Computer Won')
            play_again = input('Play again?: ')
            if play_again.lower() == 'yes' or play_again.lower() == 'y':
                game()
            else:
                quit()
        else:
            print('Human Won')
            play_again = input('Play again: ')
            if play_again.lower() == 'y' or play_again.lower() == 'yes':
                game()
            else:
                quit()


game()
