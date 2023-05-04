# Seccion 3. Archivos reales
#stream = open("/Users/carlo/Desktop/File.txt", 'rt', encoding='utf-8')

# '''
# Lectura caracter por caracter
stream = open("Text.txt", 'rt', encoding='utf-8') 
from os import strerror
try:
    counter = 0
    stream = open('text.txt', "rt", encoding='utf-8')
    char = stream.read(1)
    while char != '':
        print(char, end='')
        counter += 1
        char = stream.read(1)
    stream.close()
    print("\n\nCaracteres en el archivo:", counter)
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))


 # Lectura de todo el archivo a la vez
from os import strerror
try:
    counter = 0
    stream = open('text.txt', "rt")
    content = stream.read()
    for char in content:
        print(char, end='')
        counter += 1
    stream.close()
    print("\n\nCaracteres en el archivo:", counter)
except IOError as e:
    print("Se produjo un error de E/S: ", strerr(e.errno))


# 4.3.2 readline()
from os import strerror
try:
    character_counter = line_counter = 0
    stream = open('text.txt', 'rt', encoding='utf-8')
    line = stream.readline()
    while line != '':
        line_counter += 1
        for char in line:
            print(char, end='')
            character_counter += 1
        line = stream.readline()
    stream.close()
    print("\n\nCaracteres en el archivo:", character_counter)
    print("Líneas en el archivo:     ", line_counter)
except IOError as e:
    print("Se produjo un error de E/S:", strerror(e.errno))


# 4.3.3 readlines()
print("Lineas:")
stream = open('text.txt', 'rt', encoding='utf-8')
lines = stream.readlines(10)
i = 1
while len(lines) != 0:
    print(i, lines)
    lines = stream.readlines(10)
    i += 1
stream.close()

# ------------------------------------------------------------------------------

try:
    ccnt = lcnt = 0
    for line in open('text.txt', 'rt', encoding='utf-8'):
        lcnt += 1
        #print(lcnt, line)
        for ch in line:
            print(ch, end='')
            ccnt += 1
    print("\n\nCaracteres en el archivo:", ccnt)
    print("Líneas en el archivo:     ", lcnt)
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))

#------------------------------------------------------------------------------
# 4.3.4 Manejo de archivos de texto: write()
# write caracter por caracter
from os import strerror
try:
	file = open('newtext.txt', 'wt', encoding='utf-8' ) # Un nuevo archivo (newtext.txt) es creado.
	for i in range(10):
		s = "línea #" + str(i+1) + "\n"
		for char in s:
			file.write(char)
	file.close()
except IOError as e:
	print("Se produjo un error de E/S: ", strerror(e.errno))

#------------------------------------------------------------------------------
# write linea por linea
from os import strerror
try:
    file = open('newtext.txt', 'wt', encoding='utf-8')
    for i in range(10):
        file.write("línea #" + str(i+1) + "\n")
    file.close()
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))

# enviar un mensaje de tipo cadena a stderr
import sys
sys.stderr.write("Mensaje de Error")


#------------------------------------------------------------------------------
# Archivos binarios
# Los datos amorfos son datos que no tienen forma específica, son solo una serie de bytes.
# bytearray es un arreglo que contiene bytes (amorfos).
# bytearray debe ser un entero [0..255]
data = bytearray(5)   # almacena 5 bytes. son mutables y se accese por indexación 

for i in range(len(data)):
    data[i] = 10 - i

for b in data:
    print(hex(b))
data[0]=65    
print(data)    
    
#------------------------------------------------------------------------------
# write
from os import strerror
data = bytearray(10)
for i in range(len(data)):
    data[i] = ord('a') + i
    data[i] = 10 + i

try:
    bf = open('file.bin', 'wb')
    bf.write(data)
    bf.close()
except IOError as e:
    print("Se produjo un error de E/S:", strerror(e.errno))

#------------------------------------------------------------------------------
# readinto
from os import strerror
data = bytearray(10)

try:
    binary_file = open('file.bin', 'rb')
    binary_file.readinto(data)
    binary_file.close()

    for b in data:
        #print(hex(b), end=' ')
        print(b, end=' ')
except IOError as e:
    print("Se produjo un error de E/S:", strerror(e.errno))
print()    

# read 
# no utilices este tipo de lectura si no estás seguro de que el contenido del archivo se ajuste a la memoria disponible.
from os import strerror
try:
    binary_file = open('file.bin', 'rb')
    data = bytearray(binary_file.read())   # es immutable
    binary_file.close()

    for b in data:
        print(hex(b), end=' ')

except IOError as e:
    print("Se produjo un error de E/S:", strerror(e.errno))
print()


# read(n)
from os import strerror
try:
    binary_file = open('file.bin', 'rb')
    data = bytearray(binary_file.read(5))
    binary_file.close()

    for b in data:
        print(hex(b), end=' ')

except IOError as e:
    print("Se produjo un error de E/S:", strerror(e.errno))
# '''
#------------------------------------------------------------------------------
# 4.3.7 Copiando archivos:
from os import strerror

srcname = input("Ingresa el nombre del archivo fuente: ")
try:
    src = open(srcname, 'rb')
except IOError as e:
    print("No se puede abrir archivo fuente: ", strerror(e.errno))
    exit(e.errno)   # cual valor != 0 es Error	

dstname = input("Ingresa el nombre del archivo destino: ")
try:
    dst = open(dstname, 'wb')
except Exception as e:
    print("No se puede crear el archivo de destino: ", strerror(e.errno))
    src.close()
    exit(e.errno)	

buffer = bytearray(65536)   # 2^16
total  = 0
try:
    readin = src.readinto(buffer)
    while readin > 0:
        written = dst.write(buffer[:readin])
        total += written
        readin = src.readinto(buffer)
except IOError as e:
    print("No se puede crear el archivo de destino: ", strerror(e.errno))
    exit(e.errno)	
    
print(total,'byte(s) escritos con éxito')
src.close()
dst.close()
    
