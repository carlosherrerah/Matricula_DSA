# Seccion 1. Introduccion a los modulos en Python
# https://docs.python.org/3/tutorial/modules.html
# https://docs.python.org/3/library/index.html

# Cada módulo(Programa) consta de entidades
# Estas entidades pueden ser funciones, variables, constantes, clases y objetos.
# namespace: es un espacio, donde no hay dos objetos con el mismo nombre

import math, sys      # no recomendada 
import numpy as np
from numpy import *   # importa todas las entidades, aunque no recomendada, ej abs, np.abs
from math import sin, pi
from math import cos as c, tan as t 
pi = 3.1416

def abs(x):
    if x<0:
        x=x*(-1)
    return x

print(abs(sin(pi/4)/math.cos(math.pi/4)))
print(t(pi)/4)


