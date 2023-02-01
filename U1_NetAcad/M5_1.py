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

os.system("cls")

# print(randrange(1,10))

board = [[1,2,3],
         [4,5,6],
         [7,8,9]]

def display_board(board):
    print("+-------+-------+-------+")
    for i in range(3):
        for j in range(3):
            if j == 1:
                #print("|   X   |   X   |   X   |")
                print("|  ", board[i][j]," ","|  ", board[i][j]," ","|  ", board[i][j]," ","|")
            else:
                print("|       |       |       |")
        print("+-------+-------+-------+")
display_board(board)






