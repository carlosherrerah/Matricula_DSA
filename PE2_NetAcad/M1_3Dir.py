# Sección 3 – Módulos y Paquetes
# paquete = Directorio o Carpeta, varios modulos, se puede empaquetar
# modulo  = programa
# Entidades = Funciones(metodos), variables, constantes

# .pyc = python compilado en el directorio  __pycache__
# _Entidad = Será considerada como privada

# Los nombres shabang, shebang, hasbang, poundbang y hashpling 
# describen el dígrafo escrito como #!, 
# instruir cómo se debe iniciar el archivo fuente de Python en linux

# __init__.py Inicializa paquetes

# from Paquete    import modulo
# from Directorio import Programa 

# from programa   import funcion
# from a.b import c   =  La entidad c del modulo b del paquete a

# import Paquete
# import Modulo

import sys, os

for p in sys.path:
    print(p)
print()

print("Partida: ", os.getcwd())       # Saber de donde partimos

import module 
from module    import suml, prodl     # En el mismo directorio
from moduleDir import modulePrg       # En la carpeta modules 

# Python recorra el directorio para encontrar todos los módulos solicitados
rutaAbs = 'C:\\Dev\\Matricula_DSA\\PE2_NetAcad\\moduleDir'  # Se puede omitir la Unidad
rutaRel = './PE2_NetAcad\\moduleDir'
sys.path.append(rutaRel)
import modulePrg

module.__counter = module.__counter+1
print("\ncontador: ", module.__counter)

print("Bienvenido al programa")
print(__name__)
print()

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(modulePrg.suml(zeroes))
print(prodl(ones))


