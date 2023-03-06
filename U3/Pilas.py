class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

# LIFO = Last Input First Output
# UEPS = Ultima en Entrar Primera en Salir

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def getSize(self):
        return self.size
    
    def isEmpty(self):
        return True if self.size == 0 else False
        # return True if not self.size else False
        # return True if not self.head else False

    def push(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        self.size+=1

    def pop(self):
        data = None
        if not self.isEmpty(): 
            data = self.head.data
            self.head = self.head.next
            self.size-=1
        return data
    
    
    



'''        
      1       2     3 
    jesus, maria, jose
    jose=  pop()
'''
p1 = Stack()

p1.peak()
p1.push("Jesus")
p1.push("Maria")
p1.push("Jose")

print("Sacar-->")
#print(p1.pop())
#print(p1.pop())
#print(p1.pop()) 
#print(p1.pop()) 

p1.peak()




