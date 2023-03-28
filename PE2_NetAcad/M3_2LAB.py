# -----------------------------------------------------------------------------
#   LAB   Pila contadora
'''
class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val


class CountingStack(Stack):
    def __init__(self):
        # Llena el constructor con acciones apropiadas.
        Stack.__init__(self)
        self.__counter = 0

    def get_counter(self):
        # Presenta el valor actual del contador al mundo.
        return self.__counter

    def push(self, val):
        # Haz un pop y actualiza el contador.
        Stack.push(self, val)
        self.__counter+=1

    def pop(self):
        # Haz un pop y actualiza el contador.
        val = Stack.pop(self)
        self.__counter-=1
        return val

stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter())
'''
# -----------------------------------------------------------------------------
#   LAB   Colas alias FIFO 
# put enqueue:  Agregar  al principio de la lista 
# get dequeue:  Eliminar al final     de la lista
# QueueError exception cuando la lista esta vacia
'''
class Queue:
    def __init__(self):
        # Escribe el código aquí.
        self.__queue = []

    def put(self, elem):
        # Escribe el código aquí.
        self.__queue.insert(0, elem)

    def get(self):
        # Escribe el código aquí.
        if len(self.__queue) > 0:
            val = self.__queue[-1]
            del self.__queue[-1]
            return val        
        else:
            raise QueueError

class QueueError(IndexError):
    print("fuera de rango")

que = Queue()
que.put(1)
que.put("perro")
que.put(False)

try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")
'''

# -----------------------------------------------------------------------------
#   LAB   Colas alias FIFO: parte 2
class QueueError(IndexError):
    pass

class Queue:
    def __init__(self):
        # Escribe el código aquí.
        self.queue = []

    def put(self, elem):
        # Escribe el código aquí.
        self.queue.insert(0, elem)

    def get(self):
        # Escribe el código aquí.
        if len(self.queue) > 0:
            val = self.queue[-1]
            del self.queue[-1]
            return val        
        else:
            raise QueueError
        
    def getLen(self):
        return len(self.queue)        

class SuperQueue(Queue):
    # Escribe código nuevo aquí.
    def isempty(self):
        #return len(self.queue) == 0
        return self.getLen() == 0
    

que = SuperQueue()
que.put(1)
que.put("perro")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Cola vacía")
