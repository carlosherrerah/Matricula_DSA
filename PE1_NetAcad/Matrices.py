'''
def multiply_matrix(A,B):
  global C
  if  A.shape[1] == B.shape[0]:
    C = np.zeros((A.shape[0],B.shape[1]),dtype = int)
    for row in range(rows): 
        for col in range(cols):
            for elt in range(len(B)):
              C[row, col] += A[row, elt] * B[elt, col]
    return C
  else:
    return "Sorry, cannot multiply A and B."

[[sum(a*b for a, b in zip(A_row, B_col)) for B_col in zip(*B)]
    for A_row in A]
'''
# Matriz transpuesta
def imprimirMatriz(M):
  f = M.shape[0]
  c = M.shape[1]
  print(f,c)



F = 4 
C = 3
A = [[C * i + j + 1 for j in range(C)] for i in range(F)]  # 4 X 3
print(A)
imprimirMatriz(A)
