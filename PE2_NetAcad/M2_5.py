# Seccion 5. Cuatro programas simples
from operator import xor
'''
print(' '.isalpha())  # space is not alphabet

# Cifrado César.
text = input("Ingresa tu mensaje: ")
cipher = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)
print(cipher)

# Cifrado César - descifrando un mensaje.
#cipher = input('Ingresa tu criptograma: ')
text = ''
for char in cipher:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) - 1
    if code < ord('A'):
        code = ord('Z')
    text += chr(code)
print(text)    

# -----------------------------------------------------------------------------
#Procesador de Números.
line = input("Ingresa una línea de números, sepáralos con espacios: ")
strings = line.split()
total = 0
try:
    for substr in strings:
        total += float(substr)
    print("El total es:", total)
except:
    print(substr, "no es un numero.")

# -----------------------------------------------------------------------------
# Validador IBAN. (Número de cuenta bancaria internacional)
# https://en.wikipedia.org/wiki/International_Bank_Account_Number

iban = input("Ingresa un IBAN, por favor: ")
iban = iban.replace(' ','')

if not iban.isalnum():
    print("Has introducido caracteres no válidos.")
elif len(iban) < 15:
    print("El IBAN ingresado es demasiado corto.")
elif len(iban) > 31:
    print("El IBAN ingresado es demasiado largo.")
else:
    iban = (iban[4:] + iban[0:4]).upper()
    iban2 = ''
    for ch in iban:
        if ch.isdigit():
            iban2 += ch
        else:
            iban2 += str(10 + ord(ch) - ord('A'))
    iban = int(iban2)
    if iban % 97 == 1:
        print("El IBAN ingresado es válido.")
    else:
        print("El IBAN ingresado no es válido.")

# Inglés: GB72 HBZU 7006 7212 1253 00
# Francés: FR76 30003 03620 00020216907 50
# Alemán: DE02100100100152517108        

# -----------------------------------------------------------------------------
# https://en.wikipedia.org/wiki/Soundex
# https://en.wikipedia.org/wiki/Hamming_distance
# https://en.wikipedia.org/wiki/Levenshtein_distance


# -----------------------------------------------------------------------------
# LAB   Mejorando el Cifrado César
#text = input("Mensaje: ")
text = 'abcxyzABCxyz 123'
shift = 2
#while not (shift >= 1 and shift <= 25):
#    shift = int(input('No. Desplazar <1..25>: '))

cipher = ''
for char in text:
    if char.isalpha():

        # code = ord(char) + shift    
        # if char.isupper():
        #     first = ord('A')   # 65
        # else:
        #     first = ord('a')   # 97 
        # code = code - first    
        # code = code % 26
        # cipher += chr(first + code)

        if char.isupper():                              # 65..90  A..Z
            if  ord(char) > 65 + 26 - shift - 1:
                char = chr(ord(char) - 26 )
            cipher += chr(ord(char) + shift)
        else:
            if ord(char) > 65 + 26 + 32 - shift - 1 :   # 97..122  a..z
                char = chr(ord(char) - 26 )
            cipher += chr(ord(char) + shift)
    else:
        cipher += char
print(cipher)

# -----------------------------------------------------------------------------
# LAB   Palindromo
text = 'Ten animals I slam in a net'
text = text.replace(' ','')
text = text.lower()
inverse = text[::-1]
r = True if len(text) > 0 and text==inverse else False
print(r)

# -----------------------------------------------------------------------------
# LAB   anagrams: se forman dos palabras con las mismas letras
palabra1 = 'Listen'  # listen
palabra1 = palabra1.replace(' ','')
palabra1 = palabra1.lower()
palabra1 = list(palabra1)
palabra1.sort()
palabra1 = ''.join(palabra1)
print(palabra1)

palabra2 = "Silent"  #silent
palabra2 = ''.join(sorted(list(palabra2.lower().replace(' ',''))))

if len(palabra1)> 0 and palabra1 == palabra2:
    print("Anagramas")
else:
    print("No son agramas")    


# -----------------------------------------------------------------------------
# LAB   El Dígito de la Vida
date = "19991229"   # 6
date = '20000101'   # 4
date = input("AAAAMMDD: ")

if len(date) != 8 or not date.isdigit():
    print("Formato de fecha inválida.")
else:
    while len(date)>1:
        suma=0
        for x in date:
            suma =suma + int(x)
        date = str(suma)        
print(date)

# -----------------------------------------------------------------------------
# LAB   ¡Encuentra una palabra!
word = 'dog'
strn = 'vcxzxduybfdsobywuefgas'
texto = ""

start = 0
for x in word:
    resto = strn[start:]
    for y in resto:
        if x == y:
            texto+=x
            start=start+1
            break
        start=start+1

start = 0
found = True
for ch in word:
	pos = strn.find(ch, start) 
	if pos < 0:
		found = False
		break
	start = pos + 1

print(word  == texto)
print(found)
'''
# -----------------------------------------------------------------------------
# LAB   sudoku
# https://en.wikipedia.org/wiki/Sudoku
import numpy as np
A = [[2, 9, 5, 7, 4, 3, 8, 6, 1],
     [4, 3, 1, 8, 6, 5, 9, 2, 7],
     [8, 7, 6, 1, 9, 2, 5, 4, 3],
     [3, 8, 7, 4, 5, 9, 2, 1, 6],
     [6, 1, 2, 3, 8, 7, 4, 9, 5],
     [5, 4, 9, 2, 1, 6, 7, 3, 8],
     [7, 6, 3, 5, 2, 4, 1, 8, 9],
     [9, 2, 8, 6, 7, 1, 3, 5, 4],
     [1, 5, 4, 9, 3, 8, 6, 7, 2]]

A = [[1, 9, 5, 7, 4, 3, 8, 6, 2],
     [4, 3, 1, 8, 6, 5, 9, 2, 7],
     [8, 7, 6, 1, 9, 2, 5, 4, 3],
     [3, 8, 7, 4, 5, 9, 2, 1, 6],
     [6, 1, 2, 3, 8, 7, 4, 9, 5],
     [5, 4, 9, 2, 1, 6, 7, 3, 8],
     [7, 6, 3, 5, 2, 4, 1, 8, 9],
     [9, 2, 8, 6, 7, 1, 3, 5, 4],
     [2, 5, 4, 9, 3, 8, 6, 7, 1]]

for r in range(0, 9, 3):
    for c in range(0, 9, 3):
        a=[]
        for i in range(3):
            for j in range(3):
                a.append(A[r+i][c+j])
        print(r,c, sum(a))

# Generar la secuencia de numeros
a = [chr(i+48) for i in range(1, 10)]
a = [chr(ord('0')+i) for i in range(1, 10)]

r = '195743862'
r = sorted(list(r))
print(a == r)


'''
A = np.array(A)
r = np.sum(A[:])
print(r)

B = A.T
r = np.sum(B[:])
print(r)

# print("Hello World".count("lo")) # cuenta las ocurrencias

r1 = '295743861'
l1 = list(r1)
print(l1)
'''
