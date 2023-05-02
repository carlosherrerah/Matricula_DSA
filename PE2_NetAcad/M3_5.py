# Herencia

class Vehicle:
    pass

class LandVehicle(Vehicle):
    pass

class TrackedVehicle(LandVehicle):
    pass

my_vehicle = Vehicle()
my_land_vehicle = LandVehicle()
my_tracked_vehicle = TrackedVehicle()
mi_vehiculo = my_vehicle

#                  subclase    clase
print(issubclass(LandVehicle, Vehicle))  # Is LandVehicle a Vehicle     True
print(issubclass(Vehicle, Vehicle))      # Is Vehicle     a Vehicle     True
# cada clase se considera una subclase de sí misma

# si es un objeto es de cierta clase o no.
# isinstance(objectName, ClassName)
print(isinstance(my_land_vehicle, Vehicle))

for obj in [my_vehicle, my_land_vehicle, my_tracked_vehicle]:
    for cls in [Vehicle, LandVehicle, TrackedVehicle]:
        print(isinstance(obj, cls), end="\t")
    print()

# ↓ es una instancia de →	Vehicle	LandVehicle	TrackedVehicle
# my_vehicle	            True	    False	    False
# my_land_vehicle	        True	    True	    False
# my_tracked_vehicle	    True	    True	    True

# El operador 'is' verifica si dos variables, 
#    en este caso (object_one y object_two) se refieren al mismo objeto.

# las variables no almacenan los objetos en sí, 
#     sino los identificadores que apuntan a la memoria interna de Python.

print(mi_vehiculo is my_vehicle)

string_1 = "Mary tenía un "
string_2 = "Mary tenía un corderito"
string_1 += "corderito"

print(string_1 == string_2, string_1 is string_2)

#------------------------------------------------------------------------------
# Herencia multiple
print("Herencia Multiple:")
class Left:
    var = "L"
    var_left = "LL"
    def fun(self):
        return "Left"

class Right:
    var = "R"
    var_right = "RR"
    def fun(self):
        return "Right"

class Sub(Left, Right):
    pass

obj = Sub()

print(obj.var, obj.var_left, obj.var_right, obj.fun())
# Python busca componentes de objetos en el siguiente orden:

# Dentro del objeto mismo.
# En sus superclases, de abajo hacia arriba.
# Si hay más de una clase en una ruta de herencia, Python las escanea de izquierda a derecha.    

#------------------------------------------------------------------------------
# Creacion de Componentes (composicion)
import time

class Tracks:       # pistas
    def change_direction(self, left, on):
        print("pistas: ", left, on)

class Wheels:       # ruedas
    def change_direction(self, left, on):
        print("ruedas: ", left, on)

class Vehicle:
    def __init__(self, controller):
        self.controller = controller

    def turn(self, left):
        self.controller.change_direction(left, True)
        time.sleep(0.25)
        self.controller.change_direction(left, False)

wheeled = Vehicle(Wheels())
tracked = Vehicle(Tracks())

wheeled.turn(True)
tracked.turn(False)

#------------------------------------------------------------------------------
# Herencia Simple vs Herencia Multiple
# el emplear la función super() se vuelve ambiguo.
# La herencia múltiple viola el principio de responsabilidad única

# Orden de Resolución de Métodos (MRO) = Estrategia

class Top:
    def m_top(self):
        print("superior")

class Middle(Top):
    def m_middle(self):
        print("Medio")

# class Bottom(Middle):
# class Bottom(Top, Middle):   # TypeError: Cannot create a consistent method resolution order (MRO) for bases Top, Middle
class Bottom(Middle, Top):    
    def m_bottom(self):
        print("abajo")

object = Bottom()
object.m_bottom()   # abajo
object.m_middle()   # Medio
object.m_top()      # Superior

#------------------------------------------------------------------------------
# El problema del diamante

class Top:
    def m_top(self):
        print("top")

class Middle_Left(Top):
    def m_middle(self):
        print("middle_left")

class Middle_Right(Top):
    def m_middle(self):
        print("middle_right")

class Bottom(Middle_Left, Middle_Right):
	def m_bottom(self):
		print("bottom")

object = Bottom()
object.m_bottom()
object.m_middle()
object.m_top()

#------------------------------------------------------------------------------
# 3.5.10 RESUMEN DE SECCIÓN

# __str__() es responsable de convertir el contenido de un objeto en una cadena (más o menos) legible
# issubclass(Class_1, Class_2) es capaz de determinar si Class_1 es una subclase de Class_2
# isinstance(Object, Class) comprueba si un objeto proviene de una clase indicada.
# "is" comprueba si dos variables hacen referencia al mismo objeto.
# super() retorna la referencia a la superclase más cercana de la clase

class Mouse:
    Population = 0
    def __init__(self, name):
        Mouse.Population += 1
        self.name = name
 
    def __str__(self):
        return "Hola, mi nombre es " + self.name
 
class LabMouse(Mouse):
    def __str__(self):
        #return super().__str__() + ", Saludos"
        return Mouse.__str__(self) + ", Saludos"
 
professor_mouse = LabMouse("Profesor Mouse")
print(professor_mouse, Mouse.Population) # Imprime "Hola, mi nombre es Profesor Mouse 1"

