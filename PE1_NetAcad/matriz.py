import numpy as np

def multiply_matrix(A,B):
  # global C
  if  A.shape[1] == B.shape[0]:
    C = np.zeros((A.shape[0],B.shape[1]),dtype = int)
    for row in range(A.shape[0]): 
        for col in range(B.shape[1]):
            for elt in range(len(B)):
              C[row, col] += A[row, elt] * B[elt, col]
    return C
  else:
    return "Sorry, cannot multiply A and B."

# Matriz transpuesta

# Crear matriz A
F = 4
C = 3
A = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
#A = [[C * i + j + 1 for j in range(C)] for i in range(F)]  # 4 X 3
A = np.array(A)
print(A)

# Mostrar Coordenas
pos = 10
print("pos:", pos, " F:", (pos-1)//3,", " "C:",(pos-1)%3)

# B = A.T
# Crear transpuesta
B = []
for i in range(C):
  B.append([])
  for j in range(F):
      B[i].append(A[j][i]) 
B = np.array(B)
print(B); print()

# producto punto
print("Producto Punto")
print(A*B.T); print()


# producto cruz
print("Producto Cruz")
print(A@B)
print(A.dot(B))
print(np.matmul(A,B))

C = multiply_matrix(A,B)
print(C)



