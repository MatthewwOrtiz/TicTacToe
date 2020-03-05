import random

def drawBoard(board):
    print(' '+ board[7] + ' | ' + board[8] + ' | ' + board[9] )
    print('-----------')
    print(' '+ board[4] + ' | ' + board[5] + ' | ' + board[6] )
    print('-----------')
    print(' '+ board[1] + ' | ' + board[2] + ' | ' + board[3] )

def inputPlayerLetter():
    letter = ' '
    while not(letter == 'X' or letter =='O'):
        print('Choose your letter: X or O')
        letter = input().upper()

def whoGoesFirst():
    if random.randint(0,1)==0:
        return 'computer'
    else:
        return 'player'

def playAgain():
    print('Do you want to play again? (yes or no)')
    return input.lower.startswith('y')

def makeMove(board,letter,move):
    board[move] = letter