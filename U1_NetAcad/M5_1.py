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

# print(randrange(1,10))
col = 3
a=[]
board = [[1,2,3],
         [4,'X',6],
         [7,8,9]]

def display_board(board):
    print("+-------+-------+-------+")
    for i in range(3):
        for j in range(3):
            if j == 1:
                print("|  ", board[i][j-1], " ",
                      "|  ", board[i][j], " ",
                      "|  ", board[i][j+1], " ", "|")
            else:
                print("|       |       |       |")
        print("+-------+-------+-------+")
display_board(board)

def Fil(i):
    f = math.floor( i / col)
    f = f - 1 if i % int(col) == 0 else f
    return f

def Col(i):
    c = i - Fil(i) * col - 1
    return c

'''
int Fil(int i) {   // 7 = [2][0]
    double col = 3.0;
    int f;
    f = floor(i / col);
    f = (i % int(col) == 0) ? f - 1 : f;
    return f;
}

int Col(int i) {
    double col = 3.0;
    int c = i - Fil(i) * col - 1;
    return c;
}
'''

def rand5():
    i = 1
    while i <= 5:
        n = randrange(10)
        if n not in a:
            a.append(n)
            i = i + 1



rand5()
print(a)
print(Fil(7))
print(Col(7))





