# Lists in advanced applications
squares = [x ** 2 for x in range(10)]
print(squares)

board = []
 
# Lists in lists
for i in range(8):
    row = ["A" for i in range(8)]
    board.append(row)
print(board)    

print()
board = [[0 for i in range(24)] for j in range(7)]  # 7 X 24
#  print(board)
for day in board:
    print(day)

print("--->")
for day in board:
    for temp in day:
        print(board[day][temp])


