import os
from ADT import Stacks

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data

nodo1 = Node("jesus")
print(nodo1.data)
print(nodo1.getData()) 
print(nodo1.next)   

nodo1.setData("Maria")
print(nodo1.getData()) 
nodo2 = Node("JOSE")
nodo1.next= nodo2
print(nodo1.data)
print(nodo1.next.data)

Stacks.saludo()
