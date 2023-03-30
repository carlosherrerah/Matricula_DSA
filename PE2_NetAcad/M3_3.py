# Seccion 3. POO: Propiedades
# Variables de Instancia y de clase

# variable llamada __dict__ (es un diccionario)
# La variable contiene los nombres y valores de todas las propiedades (variables) que el objeto contiene actualmente.

# Variables de clase
# es una propiedad que existe en una sola copia y se almacena fuera de cualquier objeto

class ExampleClass:
    counter = 0
    def __init__(self, val = 1):
        self.__first = val
        ExampleClass.counter += 1

    def set_second(self, val = 2):
        self.second = val

example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)

example_object_2.set_second(3)

example_object_3 = ExampleClass(4)
example_object_3.__third = 5   # se crea otra variable

print(example_object_1.__dict__, example_object_1.counter)
print(example_object_2.__dict__, example_object_2.counter)
print(example_object_3.__dict__, example_object_3.counter)
print(ExampleClass.__dict__)

print(example_object_1._ExampleClass__first)


# -----------------------------------------------------------------------------
# Comprobando la existencia de un atributo
# es posible que no esperes que todos los objetos de la misma clase tengan los mismos conjuntos de propiedades.
class ExampleClass:
    attr = 1   # variable de clase
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1


example_object = ExampleClass(1)

print(example_object.a)

#print(example_object.b)
try:
    print(example_object.b)
except AttributeError:
    pass

# función que puede verificar con seguridad si algún objeto / clase contiene una propiedad específica
if hasattr(example_object, 'b'):
    print(example_object.b)

print(hasattr(ExampleClass, 'attr'))

