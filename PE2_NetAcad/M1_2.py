# Seccion 2. Módulos selectos de Python (math, random, platform)
import os
import math
from math import e, exp, log, ceil, floor, trunc
import numpy as np
from random import random, randrange, seed, randint, choice, sample

a = dir(math)
print(a)

for name in dir(math):
    print(name, end="\t")
print()

ad = math.degrees(math.pi/4)
print(ad)

print(math.e)
print(math.log(math.e))
print(math.log(100,10))  # log de 100 base 10 
print(math.log10(100))
print(math.log2(16))
print(math.log2(256))

print(pow(e, 1) == exp(log(e)))
print(pow(2, 2) == exp(2 * log(2)))
print(log(e, e) == exp(0))

print(math.hypot(3,4))

print("randrange: ")
for i in range(5):
    print(randrange(10,20), end="\t")    # [ )
print()    

print("randint: ")
for i in range(0,5):
    print(randint(10,20), end="\t")      # [ ]
print()    

print("random: ")
for i in range(0,5,1):
    print(random(), end="\t")
print()

seed(0)
for i in range(5):
    print(random(), end="\t")
print()

seed(0)         # para todos coincidir
for i in range(5):
    print(random(), end="\t")
print()

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(choice(my_list))
print(sample(my_list, 1))
print(sample(my_list, 5))

import random
aleatorios = random.sample(range(1, 11), 5)
aleatorios = random.sample([x for x in range(1,11)],5)
print('Unicos', aleatorios)
random.shuffle(aleatorios)
print("Shuffle", aleatorios)

myList = []
for i in range(1, 30+1):
    myList.append(random.randint(0,20))
    unicos= list(dict.fromkeys(myList))
print("Con Duplicados", myList)
print("Sin Duplicados", unicos)

print(random.sample("ABCDEFGH", 4))

# 2.5
import platform 
from platform import platform, machine, processor, system, version, python_implementation, python_version_tuple
print(platform())
print(platform(1))
print(platform(0, 1))
print(machine())
print(processor())
print("S.O. ", system())
print("Version Windows: ", version())
print(python_implementation())
print(python_version_tuple())

# https://docs.python.org/3/py-modindex.html
import os
print(dir(os))
