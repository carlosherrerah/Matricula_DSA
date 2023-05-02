# Seccion 1. Generadores, iteradores y cierres

# Un generador de Python es un fragmento de código especializado capaz de producir una serie de valores y 
#    controlar el proceso de iteración. los generadores a menudo se llaman iteradores.
'''
for i in range(5):
    print(i)

# Fib[i] = Fib[i-1] + Fib[i-2]
class Fib:
    def __init__(self, nn):
        print("__init__")
        self.__n = nn
        self.__i = 0
        self.__p1 = self.__p2 = 1
    
    def __iter__(self):
        print("__iter__")
        return self
    
    def __next__(self):
        print("__next__", self.__i, end= "\t")		
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret

for i in Fib(5):
    print(i)
print()    

class Class:
    def __init__(self, n):
        self.__iter = Fib(n)

    def __iter__(self):
        print("Class iter")
        return self.__iter

object = Class(5)
for i in object:
    print(i)

# 4.1.2 La sentencia yield
# Se puede ver la palabra "yield" como un hermano más inteligente de la sentencia "return"

def fun(n):
    for i in range(n):
        yield i

for v in fun(5):
    print(v)    


def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2
 
print() 
for v in powers_of_2(5):
    print(v)

# Lista por comprension
v = [x for x in powers_of_2(5)]
print(v)

# La funcion list()
l = list(powers_of_2(5))
print(l)


# Usando yield
def fib(n):
    p1 = p2 = 1

    for i in range(n):
        i += 1  
        if i > n:
            raise StopIteration
        if i in [1, 2]:
            yield 1
            continue
        ret = p1 + p2
        p1, p2 = p2, ret
        yield ret

for v in fib(10):
    print(v) 


def fibonacci(n):
    p1 = p2 = 1
    for i in range(n):
        if i in [0, 1]:
            yield 1
        else:
            n = p1 + p2
            p2, p1 = p1, n
            yield n

fibs = list(fibonacci(10))
print(fibs)
 


list_1 = []
for ex in range(6):
    list_1.append(10 ** ex)

list_2 = [10 ** ex for ex in range(6)]   # Listas por comprension

print(list_1)
print(list_2)

# Listas por comprension
the_list      = [1 if x % 2 == 0 else 0 for x in range(10)]   # Los corchetes  hacen una comprension
the_generator = (1 if x % 2 == 0 else 0 for x in range(10))   # Los parentesis hacen un  generador
print(the_list)
print(the_generator)

for v in the_list:
    print(v, end=" ")
print()

for v in the_generator:
    print(v, end=" ")
print()

'''
#------------------------------------------------------------------------------
# 4.1.5 La función lambda
# Una función lambda es una función sin nombre (también puedes llamarla una función anónima)
# lambda parameters: expression

two = lambda: 2
doble = lambda x: 2*x
pwr = lambda x, y : x ** y
lista= [x for x in range(5)]

print(two())
print(doble(5))
print(pwr(2,3))
y=(lambda x:x+3)(4)
print(y)

# map(function, list)   devuelve un iterador o generador
y=list(map(lambda x:x*2,lista))
print(y)

for x in map(lambda x:2*x, lista):
    print(x, end= " ")
print()    

mayores = list(filter(lambda x: x>2, lista))
print(mayores)

# f(x) = 2x^2 - 4x + 2
def print_function(args, fun):
    for x in args:
        print('f(', x,')= ', fun(x), sep='')

def poly(x):
    return 2 * x**2 - 4 * x + 2

# print_function([x for x in range(-2, 3)], poly)
print_function([x for x in range(-2, 3)], lambda x: 2 * x**2 - 4 * x + 2)

# filter
from random import seed, randint

seed()
data = [randint(-10,10) for x in range(5)]
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data)) # pares mayores a 0

print(data)
print(filtered)

# 4.1.9 Una breve explicación de cierres ??
def make_closure(par):
    loc = par

    def power(p):
        return p ** loc
    return power


fsqr = make_closure(2)
fcub = make_closure(3)

for i in range(5):
    print(i, fsqr(i), fcub(i))

# 4.1.10 RESUMEN DE SECCIÓN
# Un iterator es un objeto de una clase que proporciona al menos dos métodos (sin contar el constructor):

# __iter__() se invoca una vez cuando se crea el iterador y devuelve el propio objeto del iterador.
# __next__() se invoca para proporcionar el valor de la siguiente iteración 
#     y genera la excepción StopIteration cuando la iteración llega a su fin.

# La sentencia yield suspende la ejecución de la función y 
#    hace que la función regrese el argumento de yield como resultado

# Una lista por comprensión se convierte en un generador cuando se emplea dentro de paréntesis 
#     (usado entre corchetes, produce una lista regular).
for x in (el * 2 for el in range(5)):
    print(x)

# Una función lambda es una herramienta para crear funciones anónimas
def foo(x, f):
    return f(x)
 
print(foo(9, lambda x: x ** 0.5))
     
# Convertir todas a mayusculas
short_list = ['mython', 'python', 'cayó', 'en', 'el', 'piso'] 
new_list = list(map(lambda s:s.upper() , short_list))
print(new_list)

# filtrar los strings
short_list = [1, "Python", -1, "Monty"]
new_list = list(filter(lambda s: isinstance(s, str), short_list))
print(new_list)

# Cierre
def tag(tg):
    tg2 = tg
    tg2 = tg[0] + '/' + tg[1:]
 
    def inner(str):
        return tg + str + tg2
    return inner
  
b_tag = tag('<b>')
print(b_tag('Monty Python'))

# 4.1.11 CUESTIONARIO DE SECCIÓN
class Vowels:
    def __init__(self):
        self.vow = "aeiou "
        self.pos = 0
 
    def __iter__(self):
        return self
 
    def __next__(self):
        if self.pos == len(self.vow):
            raise StopIteration
        self.pos += 1
        return self.vow[self.pos-1]
  
vowels = Vowels()
for v in vowels:
    print(v, end=' ')
print()

# Cierre: Reemplaza los ' ' por *
def replace_spaces(replacement = '*'):
    def new_replace(text):
        return text.replace(' ', replacement)
    return new_replace
  
starts = replace_spaces()
print(starts('I love you'))

# Recomendado:
def f(x): return 3*x
 
# No recomendado:
f = lambda x: 3*x

print(f(3))
