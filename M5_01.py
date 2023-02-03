# separacion de digitos
a = 353
b = str(a)
c = list([int(x) for x in b])
print(c)

# unir la cadena
A = ["a", "b", "c"]
StrA = "".join(A)
print(StrA)

# unir los numeros
a = [1,2,3]
a.reverse()

b = "".join([str(_) for _ in a])
print(b)

# a=[]
# a[0].append(3)
# a[0].append(5)
# a[1].append(4)
# a[1].append(8)
print(a)

import random
n = 4
m = 3
matriz = []

for i in range(n):
    matriz.append([])
    for j in range(m):
        matriz[i].append(random.randint(0, 100))
print(matriz)

texto="somos o no somos"
# mayores = list(filter(lambda x: x>2, lista))
x = texto.split()
strA = "".join(x)
# strB = strA.__reversed__()
print(strA)

class Numbers:
    def __init__(self):
        self.numbers = [1, 2, 3, 4, 5]
    def __reversed__(self):
        for number in self.numbers[::-1]:
            yield number
numbers_obj = Numbers()
for number in reversed(numbers_obj):
    print(number)