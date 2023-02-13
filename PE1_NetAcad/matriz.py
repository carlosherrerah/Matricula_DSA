import numpy as np
import ctypes

def multiply_matrix(A,B):
  # global C
  if  A.shape[1] == B.shape[0]:
    C = np.zeros((A.shape[0],B.shape[1]),dtype = int)
    for i in range(A.shape[0]):       # M 
        for j in range(B.shape[1]):   # N
            for k in range(len(B)):   # P
              # C[i, j] += A[i, k] * B[k, j]  # Funciona
              C[i][j] += A[i][k] * B[k][j]    # Funciona 
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
print(len(C))     # No. de Renglones
print(np.size(C)) # No. de elementos
print("Adress of C:", id(C))
print("Adress of C:", id(C)+1)
print(C[0][0], C[0,0])

val_mi_id = ctypes.cast(id(C), ctypes.py_object).value
print(val_mi_id[0][1])
print(val_mi_id)

print(f"{val_mi_id = }")

