""" comments
import mypkg.sibling
from mypkg import sibling
""" 
# hash


# PEP 8 -- Style Guide for Python Code
# https://peps.python.org/pep-0008/

# variables = containers = boxes
# Python is a dynamically-typed language
_n = 1
n = 2
N = 3
_1 = 10
exchange_rate = None

m = 5
m = "Hello"

keywords = ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 
            'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 
            'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 
            'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield','True']
keywords.insert(2,"Hola")

print("Conteo", len(keywords))

print(keywords)

print(keywords[-1], keywords.index('True'))
print(keywords.pop(), keywords.pop(), keywords.pop(1), keywords[1] )

x=2
x+=1      # Shortcut operators
print(x)
print(round(3.14159,4))

y = "5" + "2"   # concatenate
print(y)

a = 6
b = 3
a /= 2 * b    # a = a / ( 2 * b) 
print(a) 
