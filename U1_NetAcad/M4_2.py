# How functions communicate with their environment

# parameters live inside functions (this is their natural environment)
# arguments exist outside functions, and are carriers of values passed to corresponding parameters.

# Positional parameter passing
# Keyword argument passing
# Mixing positional and keyword arguments
#        positional arguments before keyword arguments.


def potencia(base, exponente):
    return base**exponente

y = potencia(2,3)
y = potencia(exponente=3, base= 2)




