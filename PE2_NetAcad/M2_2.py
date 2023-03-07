# Sección 2 – La naturaleza de las cadenas en Python
# las cadenas de Python son secuencias inmutables
# diagonal invertida (\) empleada como un carácter de escape, 
#    no esta incluida en la longitud total de la cadena.

i_am = 'I\'m'
print(len(i_am))

# comilla simple(apostrofe) o doble
multiline = '''Línea #1
Línea #2'''
print(len(multiline))  # Cuenta ademas el salto de línea \n(invisible)
print(multiline)
print()

# Las cadenas pueden ser Concatenadas (unidas) o Replicadas
str1 = 'a'
str2 = 'b'
print(str1 + str2)
print(str2 + str1)
print(5 * 'a')
print('b' * 4)
print()

# Demostración de la función ord().
char_1 = 'a'
char_2 = ' '  # space
print(ord(char_1))
print(ord(char_2))
print(ord('α'))
print()

# Demostración de la función chr().
print(chr(97))
print(chr(945))
print(chr(ord('a'))=='a')

# 2.4 Cadenas como Secuencias
texto = "Hello World"
for i in range(len(texto)):
    #print(texto[i],    end= ' ')
    print(texto[-i-1], end= ' ')     # Reverse
print()    

for char in texto:
    print(char, end= ' ') 
print()    

a = texto[::-1]                      # Reverse
print(a)

# Rebanadas
alpha = "abdefg"
#        012345  [inicial:final:incremento]
print(alpha[1:3])  # bd
print(alpha[3:])   # efg
print(alpha[:3])   # abd
print(alpha[3:-2]) # e
print(alpha[-3:4]) # e
print(alpha[::2])  # adf
print(alpha[1::2]) # beg
print()

print("F" in alpha)
print("Ef" in alpha)
print("F" not in alpha)


alphabet = "bcdefghijklmnopqrstuvwxy"
alphabet = "a" + alphabet
alphabet = alphabet + "z"
print(alphabet)
print(min(alphabet), max(alphabet))

lista = [2,5,1]
print(min(lista))
print(alphabet.index("c"))   # Regresa el index o posicion, error si no existe

lista = list(alphabet)
print(lista)

# Demostración del método count():
print("abcabc".count("b"))
print('abcabc'.count("d"))

# Funciones de cadenas
# https://docs.python.org/3.4/library/stdtypes.html#string-methods
print("universidad".replace("sida", "vih"))
print('1,2,3'.split(','))
print("pi"*2)












