# tic tac toe
# X = computer
# O = user
# X comienza en casilla 5
# El programa checa si es over:
#    continuar
#    empate
#    Tu ganas
#    La PC gana

# board[row][column]     X  O  n

# import random
from random import randrange
import os
import math

os.system("cls")
col = 3

# print(randrange(1,10))

def Fil(i):
    f = math.floor(i / col)
    f = f - 1 if i % int(col) == 0 else f
    return f


def Col(i):
    c = i - Fil(i) * col - 1
    return c


'''
def display_board(board):
    print("+-------+-------+-------+")
    for i in range(3):
        for j in range(3):
            if j == 1:
                print("|  ", board[i][j-1], " ",
                      "|  ", board[i][j],   " ",
                      "|  ", board[i][j+1], " ", "|")
            else:
                print("|       |       |       |")
        print("+-------+-------+-------+")
'''

def display_board(board):
    print("+-------" * 3, "+", sep="")
    for row in range(3):
        print("|       " * 3, "|", sep="")
        for col in range(3):
            print("|   " + str(board[row][col]) + "   ", end="")
        print("|")
        print("|       " * 3, "|", sep="")
        print("+-------" * 3, "+", sep="")

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.
    while True:
        pos = int(input("Enter your move: "))

        f = Fil(pos)
        c = Col(pos)

        f = (pos - 1) // 3   # 0 .. 8
        c = (pos - 1) % 3

        if board[f][c] not in ['O', 'X']:
            board[f][c] = 'O'
            break
    #display_board(board)


def draw_move(board):
    # The function draws the computer's move and updates the board.
    free = make_list_of_free_fields(board)  # make a list of free fields
    cnt = len(free)
    if cnt > 0:  # if the list is not empty, choose a place for 'X' and set it
        this = randrange(cnt)
        row, col = free[this]
        board[row][col] = 'X'


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free = []
    for i in range(3):
        for j in range(3):
            if type(board[i][j]) is int:
                free.append((i, j))
    return free


def victory_for(board, sgn):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game
    if sgn == "X":  # are we looking for X?
        who = 'me'  # yes - it's computer's side
    elif sgn == "O":  # ... or for O?
        who = 'you'  # yes - it's our side
    else:
        who = None  # we should not fall here!
    cross1 = cross2 = True  # for diagonals

    for rc in range(3):
        if board[rc][0] == sgn and board[rc][1] == sgn and board[rc][2] == sgn:  # check row rc
            return who
        if board[0][rc] == sgn and board[1][rc] == sgn and board[2][rc] == sgn:  # check column rc
            return who
        if board[rc][rc] != sgn:  # check 1st diagonal
            cross1 = False
        if board[2 - rc][2 - rc] != sgn:  # check 2nd diagonal
            cross2 = False
        if cross1 or cross2:
            return who
        return None

def rand5():
    i = 1
    while i <= 5:
        n = randrange(10)
        if n not in a:
            a.append(n)
            i = i + 1

a = []
board = [[1, 2, 3],
         [4, 'X', 6],
         [7, 8, 9]]

board = [ [3 * i + j + 1 for j in range(3)] for i in range(3) ] # make an empty board
board[1][1] = 'X' # set first 'X' in the middle
free = make_list_of_free_fields(board)
human_turn = True # which turn is it now?
while len(free):
	display_board(board)
	if human_turn:
		enter_move(board)
		victor = victory_for(board,'O')
	else:	
		draw_move(board)
		victor = victory_for(board,'X')
	if victor != None:
		break
	human_turn = not human_turn		
	free = make_list_of_free_fields(board)

display_board(board)
if victor == 'you':
	print("You won!")
elif victor == 'me':
	print("I won")
else:
	print("Tie!")
        
r = math.pow(25,0.5) 

print(r)       
print(". . . Hecho")

