'''
# Seccion 4. POO: metodos
# un método es una función que está dentro de una clase.
# un método está obligado a tener al menos un parámetro.
# un método puede invocarse sin un argumento, pero no puede declararse sin parámetros.
# El primer (o único) parámetro generalmente se denomina self
# self: identifica el objeto para el cual se invoca el método.
# El parámetro self es usado para obtener acceso a la instancia del objeto y las variables de clase.
# El parámetro self también se usa para invocar otros métodos desde dentro de la clase.
# un método cuyo nombre comienza con __ está (parcialmente) oculto.

# Si una clase contiene un constructor (un método llamado __init__), 
#    este no puede devolver ningún valor y no se puede invocar directamente.


class Classy:
    varia = 1
    def __init__(self, value):
        self.var = value

    def other(self):
        print("otro")
        print(self.var)
 
    def method(self):
        print("método")
        self.other()

    def __hidden(self):
        print("oculto")

# __bases__ es una tupla. La tupla contiene clases. solo las clases tienen este atributo, los objetos no.
# __bases__ es una tupla que contiene las superclases de una clase.
def printBases(cls):    # Indica la clase padre
    print('( ', end='')
    for x in cls.__bases__:
        print(x.__name__, end=' ')
    print(')')


obj = Classy("Hola")
obj.method()

try:
    obj.__hidden()
except:
    print("fallido")
 
obj._Classy__hidden()

# 4.2 La vida al interior de las clases y objetos
print(obj.__dict__)
print(Classy.__dict__)

# Nombre de la clase o donde esta viviendo
print(Classy.__name__)
print(type(obj).__name__)

# almacena el nombre del módulo que contiene la definición de la clase
# cualquier módulo llamado __main__  es el archivo actualmente en ejecución.
print(Classy.__module__)
print(obj.__module__)

printBases(Classy)


# 4.3 Reflexión e introspección
# Introspección: es la capacidad de un programa para examinar el tipo o 
#                las propiedades de un objeto en tiempo de ejecución.
# Reflexión: es la capacidad de un programa para manipular los valores, 
#            propiedades y/o funciones de un objeto en tiempo de ejecución.

class MyClass:
    pass


obj = MyClass()
obj.a = 1
obj.b = 2
obj.i = 3
obj.ireal = 3.5
obj.integer = 4
obj.z = 5


def incIntsI(obj):
    for name in obj.__dict__.keys():
        if name.startswith('i'):
            val = getattr(obj, name)
            if isinstance(val, int):
                setattr(obj, name, val + 1)


print(obj.__dict__)
incIntsI(obj)
print(obj.__dict__)

'''
class Snake:
    def __init__(self):
        self.victims = 0

    def __init__(self, value):
        self.victims = value

    def increment(self):
        self.victims += 1

class Python(Snake):
    pass

print(Python.__name__, 'es una', Snake.__name__)
print(Python.__bases__[0].__name__, 'puede ser una', Python.__name__)


