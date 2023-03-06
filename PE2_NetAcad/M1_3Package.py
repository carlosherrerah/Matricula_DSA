import os

from sys import path
rutaAbs = 'C:\\Dev\\Matricula_DSA\\packages'
rutaRel = './Packages'
rutaZip = 'C:/Dev/Matricula_DSA/packages/extrapack.zip'
path.append(rutaZip)

import extra.good.best.sigma as sig
import extra.good.alpha as alp
from extra.iota import FunI
from extra.good.beta import FunB

print("Partida: ", os.getcwd())      # Saber de donde partimos
print(sig.FunS())
print(alp.FunA())
print(FunI())
print(FunB())


