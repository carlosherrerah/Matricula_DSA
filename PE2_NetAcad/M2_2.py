# Sección 2 – La naturaleza de las cadenas en Python
# las cadenas de Python son secuencias inmutables
# diagonal invertida (\) empleada como un carácter de escape, 
#    no esta incluida en la longitud total de la cadena.

i_am = 'I\'m'
print(len(i_am))

# '''   o   """"
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

