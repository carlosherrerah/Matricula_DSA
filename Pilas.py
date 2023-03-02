class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

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
      1       2     3 
    jesus, maria, jose
    jose=  pop()

    pop 
    push
    show
    content
