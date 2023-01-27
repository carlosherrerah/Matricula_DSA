# How functions communicate with their environment

# parameters live inside functions (this is their natural environment)
# arguments exist outside functions, and are carriers of values passed to corresponding parameters.

# Positional parameter passing
# Keyword argument passing
# Mixing positional and keyword arguments
#        positional arguments before keyword arguments.

def saludo(name):
    print("Welcome to Python:", name)

def potencia(base, exponente=2): # default or predefined
    return base**exponente

name = input("Name: ")
saludo(name)

y = potencia(2,3)
y = potencia(exponente=3, base= 2)
y = potencia(2, exponente=3)
y = potencia(2)

# y = cuadratica1(1, c=15, b= -8)
print(y)

'''
def add_numbers(a, b=2, c):
    print(a + b + c)
add_numbers(a=1, c=3)
'''









