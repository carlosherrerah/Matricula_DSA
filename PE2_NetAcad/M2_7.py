# Seccion 7. La anatomia de las Excepciones
# Python 3 define 63 excepciones integradas
# ¡El orden de las excepciones importa!
# No coloques excepciones más generales antes que otras más concretas.

# except (ValueError, TypeError):    # 2 o mas excepciones

y=1
if y==0:
    #raise AssertionError()
    raise ZeroDivisionError()

y=1
assert y==1   # afirmar, de lo contrario es un AssertionError
# genera la excepcion cuando la expresión es igual a cero, una cadena vacía o None.
# Las aserciones no reemplazan las excepciones ni validan los datos, son suplementos.
import math
x = float(input("Ingresa un número: "))
assert x >= 0.0
x = math.sqrt(x)
print(x)

def foo(x):
    assert x
    return 1/x
 
try:
    print(foo(0))
except ZeroDivisionError:
    print("cero")
except:
    print("algo")