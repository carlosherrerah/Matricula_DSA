class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data
    
    def setData(self, dato):
        self.data= dato

nodo1 = Node("Jesus")
print(nodo1.data)
print(nodo1.getData()) 
print(nodo1.next)  

nodo1.setData("Maria")
print(nodo1.getData()) 
print(nodo1.data) 

nodo2 = Node("JOSE")
nodo1.next= nodo2

nodo3 = Node("Jesus")
nodo2.next = nodo3

print("----->")
print(nodo1.data)
print(nodo1.next.data)
print(nodo1.next.next.data)
print(nodo1.next.next.next)

print(nodo1.next.next.next.data)



    
    
