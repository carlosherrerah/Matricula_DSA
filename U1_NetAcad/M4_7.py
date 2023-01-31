# Excepciones
# bug = bichos
 
import os 
import unittest as ut

print(type(5) is int)
os.system("cls")
# aislar el problema
# course: Testing Essentials with Python

y=1
assert y==1

if y==0:
    raise AssertionError()

try: 
    y = 5/0
    print("Hello")
except ZeroDivisionError: 
    print("No permitida la division entre 0")
except (ValueError, TypeError):
    print("valor incorrecto")    
except:
    print("division by zero")
finally:
    print("Cool")
print(". . . Hecho")
# https://docs.python.org/3/library/exceptions.html

# pruebas unitarias: Asignar diferentes valores 

# bug vs debug
# IDLE = Integrated Development and Learning Environment
# IDLE = Entorno de Desarrollo y Aprendizaje Integrado
      

