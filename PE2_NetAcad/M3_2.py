# Seccion 2. De procedimental a Orientado a objetos
# La capacidad de ocultar (proteger) los valores seleccionados contra el acceso no autorizado se llama encapsulamiento

# PILAS: UEPS = LIFO (Last In- First Out)

# Pila:  Enfoque Procedimental
stack = []
# stack.append(5)
# stack.pop()

def push(val):
    stack.append(val)

def pop():
    val = stack[-1]
    del stack[-1]
    return val

push(1)
push(2)
stack[0]=0

print(pop())
print(pop())

# ¿Que pasa si requieres de otra pila? Los metodos ya no son efectivos
# Pila:  Enfoque Orientado a Objetos
# constructor: construir un nuevo objeto y la inicializacion

# Cuando cualquier componente de la clase tiene un nombre que comienza con dos guiones bajos (__), 
#    se vuelve privado, esto significa que solo se puede acceder desde dentro de la clase.
#     Así es como Python implementa el concepto de encapsulación
# Todos los métodos deben tener este parámetro "self" invoca al objeto actual

class Stack:
    def __init__(self):    # Constructor
        #print("Hola")
        self.__stack=[]    # private
        self.stack=[]      # public 

    def push(self, val):
        self.__stack.append(val)

    def pop(self):
        val = self.__stack[-1]
        del self.__stack[-1]
        return val


stack1 = Stack()
stack2 = Stack()

print(len(stack1.stack))

stack1.push(1)
stack1.push(2)
print(stack1.pop())
print(stack1.pop())

# invocar cualquier método (incluidos los constructores) desde fuera de la clase nunca requiere colocar el argumento self en la lista de argumentos, 
# invocar un método desde dentro de la clase exige el uso explícito del argumento self, y tiene que ser el primero en la lista.
class AddingStack(Stack):     # Extend o Herencia
    def __init__(self):
        Stack.__init__(self)  # Python te obliga a invocar explícitamente el constructor de una superclase.
        self.__sum = 0        # private

    def push(self, val):
        self.__sum += val
        Stack.push(self, val)

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val   
        return val
    
    def get_sum(self):      # Encapsulacion          
        return self.__sum

stack_object = AddingStack()

for i in range(5):
    stack_object.push(i)
print("suma: ", stack_object.get_sum())

for i in range(5):
    print(stack_object.pop())







