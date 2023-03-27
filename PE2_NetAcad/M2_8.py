# Seccion 8. Prueba del Modulo 
# https://docs.python.org/3.6/library/exceptions.html
# http://www.w3big.com/
# https://www.w3schools.com/


'''
# -----------------------------------------------------------------------------
from math import tan, radians
angle = int(input('Ingresa un angulo entero en grados: '))
 
# Debemos estar seguros de que angle != 90 + k * 180
assert angle % 180 != 90
print(tan(radians(angle)))
 
# -----------------------------------------------------------------------------
the_list = [1, 2, 3, 4, 5]
ix = 0
do_it = True
 
while do_it:
    try:
        print(the_list[ix])
        ix += 1
    except IndexError:
        do_it = False
 
print('Listo')


# -----------------------------------------------------------------------------
# Este código no puede ser abortado por Ctrl-C.
from time import sleep
 
seconds = 0
while True:
    try:
        print(seconds)
        seconds += 1
        sleep(1)
    except KeyboardInterrupt:
        print("¡No hagas eso!")


# -----------------------------------------------------------------------------
# ¿Cómo abusar del diccionario
# y cómo lidiar con ello?

dictionary = {'a': 'b', 'b': 'c', 'c': 'd'}
ch = 'a'

print(dictionary[dictionary[ch]])
try:
    while True:
        ch = dictionary[ch]
        print(ch)
except KeyError:
    print('No existe tal clave:', ch)
''' 
# -----------------------------------------------------------------------------
#   LAB   Leyendo enteros de manera segura
def read_int(prompt, min, max):
    ok = False
    while not ok:    # ok == False:
        try:
            v = int(input(prompt))
            if  not (v>=min and v<=max):
                raise Exception
            ok = True
        except ValueError:
            print("Entrada Incorrecta")
        except:
            print("Rango no Permitido")
    return v

v = read_int("Numero <-10 a 10>: ", -10, 10)
print("El número es: ", v)

