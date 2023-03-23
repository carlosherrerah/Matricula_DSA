# Seccion 6. Errores: el pan diario del programador
import math

x = float(input("Ingresa x: "))
if type(x) is float:
    print("float")
assert x > 0

if type(x) is not float:
    raise AssertionError()

y = math.sqrt(x)
print("La raíz cuadrada de", x, "es igual a", y)

