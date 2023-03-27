# Seccion 6. Errores: el pan diario del programador   M4_7
import math

'''
x = float(input("Ingresa x: "))

if type(x) is float:
    print("float")
assert x > 0

if type(x) is not float:
    raise AssertionError()

result = isinstance(x, float)
print(result)

y = math.sqrt(x)
print("La raíz cuadrada de", x, "es igual a", y)
'''

try:
    x = float(input("Ingresa x: "))    
    print(math.sqrt(x))
    print("Operacion Exitosa")
except ValueError:
    print("Debes ingresar un valor positivo...")    
except ZeroDivisionError:
    print("Error en Indice")    
except:
    print("Oh Cielos, algo salio mal.")
print("FIN.")

a = [3,2,6,5,7]
print(a[2//1])
print(a[2*1])
# print(a[2/1])    # Error
# print(a[2*1.0])  # Error

