# Seccion 6. Mas sobre excepciones

'''
def reciprocal(n):
    try:
        n = 1 / n
    except ZeroDivisionError:
        print("División fallida")
        n = None
    else:      # No ha habido exception   
        print("Todo salió bien")
    finally:   # Es siempre ejecutado
        print("Es momento de decir adiós")
        return n

print(reciprocal(2))
print(reciprocal(0))


try:   # Las excepciones son clases
    i = int("¡Hola!")
except Exception as e:   # permite interceptar un objeto 
    print(e)
    print(e.__str__())

# todas las clases de excepción predefinidas en forma de árbol.
def print_exception_tree(thisclass, nest = 0):
    if nest > 1:
        print("   |" * (nest - 1), end="")
    if nest > 0:
        print("   +---", end="")

    print(thisclass.__name__)

    for subclass in thisclass.__subclasses__():
        print_exception_tree(subclass, nest + 1)

# print_exception_tree(BaseException)
# print_exception_tree(Exception)
print_exception_tree(ValueError)

# 3.6.3 Anatomía detallada de las excepciones
def print_args(args):
    lng = len(args)
    if lng == 0:
        print("")
    elif lng == 1:
        print(args[0])
    else:
        print(str(args))

try:
    raise Exception
except Exception as e:
    print(e, e.__str__(), sep=' : ' ,end=' : ')
    print_args(e.args)

try:
    raise Exception("mi excepción")
except Exception as e:
    print(e, e.__str__(), sep=' : ', end=' : ')
    print_args(e.args)

try:
    raise Exception("mi", "excepción")
except Exception as e:
    print(e, e.__str__(), sep=' : ', end=' : ')
    print_args(e.args)
'''
	
# 3.6.4 Cómo crear tu propia excepción
class PizzaError(Exception):
    def __init__(self, pizza='desconocida', message=''):
        Exception.__init__(self, message)
        self.pizza = pizza
 
 
class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza='desconocida', cheese='>100', message=''):
        PizzaError.__init__(self, pizza, message)
        self.cheese = cheese
 
 
def make_pizza(pizza, cheese):
    if pizza not in ['margherita', 'capricciosa', 'calzone']:
        raise PizzaError
    if cheese > 100:
        raise TooMuchCheeseError
    print("¡Pizza lista!")
 
 
for (pz, ch) in [('calzone', 0), ('margherita', 110), ('mafia', 20)]:
    try:
        make_pizza(pz, ch)
    except TooMuchCheeseError as tmce:
        print(tmce, ':', tmce.cheese)
    except PizzaError as pe:
        print(pe, ':', pe.pizza)
       
# Cuestionario de Seccion
import math
 
class NewValueError(ValueError):
    def __init__(self, name, color, state):
        self.data = (name, color, state)
 
try:
    raise NewValueError("Advertencia enemiga", "Alerta roja", "Alta disponibilidad")
except NewValueError as nve:
    for arg in nve.args:
        print(arg, end='! ')

