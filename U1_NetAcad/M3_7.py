# Lists in advanced applications
import numpy as np

squares = [x ** 2 for x in range(10) if x**2 % 2 ==0]
print(squares)

board = []
 
# Lists in lists
for i in range(8):
    row = ["A" for i in range(8)]
    board.append(row)
print(board)    

a = np.array([7,2,4])
b = np.array([[1, 2, 3, 6],
              [4, 5, 6, 15],
              [7, 8, 9, 24]])  # 3 X 4

c = np.array([[[2,17,23,1],[45,78,45,3],[5,6,7,8]],
              [[9,27,13,9],[35,68,35,5],[1,2,3,4]]])
print("c" , c.shape)  # 2,3,4
print(c[1][2][3])
             
print(b.shape)
print(b.shape[0])
print(b[2,1])
print("np.where", np.where(a > 3))

board1 = [[i+j for j in range(3)] for i in range(7)]  # 7 X 3
board2 = np.array(board1)
print("F, C", board2.shape)
print("Len ", len(board2))
print(board2) ; print()

print("Days")
for day in board1:
    print(day)
print()    

for day in board2:
    for item in day:
        print(item, end="\t")
    print()
print()    

for i in range(board2.shape[0]):
    for j in range(board2.shape[1]):
        print(board2[i][j], end="\t")
    print() 
print()

# 3 bildings, 15 floors each, 20 rooms on each floor
# True = Occupied
# How many vacancies are there in the 15th floor of the third building? 
rooms = [[[False for r in range(20)] for f in range(15)] for b in range(3)]
       



