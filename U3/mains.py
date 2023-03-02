# import module 
from module import suml, prodl
print("Bienvenido al programa")
print(__name__)

"""
print(module.__counter)
module.__counter = module.__counter+1
print(module.__counter)
"""
zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(suml(zeroes))
print(prodl(ones))