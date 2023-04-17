from queue import Queue
from collections import deque

class Node:
    def __init__(self, data):
        self.data  = data
        self.left  = None
        self.right = None

    def getData(self):
        return self.data

class Tree:
    def __init__(self):
        self.root = None
        self.size = 0

    def getSize(self):
        return self.size

    def isEmpty(self):
        # return True if self.size == 0 else False ?
        return True if not self.root else False

    def preorder(self, node):
        if node:
            print(node.data, end=' ')
            self.preorder(node.left)
            self.preorder(node.right)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=' ')
            self.inorder(node.right)

    def postorder(self, node):
        if (node != None):
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=' ')

    def insert(self, data):
        newNode =  Node(data)
        self.size+=1
        if self.root == None:
            self.root = newNode
        else:
            self.insertNode(self.root, newNode)

    def insertNode(self, node, newNode):
        if newNode.data <= node.data:
            if node.left == None:
                node.left = newNode
            else:
                self.insertNode(node.left, newNode)
        else:
            if node.right == None:
                node.right = newNode
            else:
                self.insertNode(node.right, newNode)

    def maxDepth(self, node):    # niveles (maxima profundidad o altura) 
        if node == None:
            return -1
        else:
            # /* compute the depth of each subtree */
            lDepth = self.maxDepth(node.left)
            rDepth = self.maxDepth(node.right)
            return (lDepth + 1) if lDepth > rDepth else rDepth + 1
            # return (lDepth > rDepth) ? (lDepth + 1) : (rDepth + 1);

    def graficarArbol(self, nodo_actual, prefix="", is_left=True):
        if nodo_actual is not None:
            self.graficarArbol(nodo_actual.right, prefix + ("│   " if is_left else "    "), False)
            print(prefix + ("└── " if is_left else "┌── ") + str(nodo_actual.data))
            self.graficarArbol(nodo_actual.left, prefix + ("    " if is_left else "│   "), True)

    def niveles_arbol(self):
        niveles = []
        queue = [self.root]
        while queue:
            nivel = []
            for i in range(len(queue)):
                node = queue.pop(0)
                if node:
                    nivel.append(node.data)
                    queue.append(node.left)
                    queue.append(node.right)
            if nivel:
                niveles.append(nivel)

        return niveles

    def imprimirAnchura(self, node, nivel):  #+-
        if node != None:
            self.imprimirAnchura(node.left, nivel + 1)
            print(str(node.data) + "(" + str(nivel) + ")")
            # print(node, "(", nivel,")")
            self.imprimirAnchura(node.right, nivel + 1)

    def levelorder(self, root):  # +-
        if root==None:
            return
        Q=Queue()
        Q.put(root)
        while(not Q.empty()):
            node=Q.get()
            if node==None:
                continue
            print(node.data)
            Q.put(node.left)
            Q.put(node.right)

    def nivel(self):   # +-
        if self.root is None:
            return
        
        cola = deque()
        cola.append(self.root)
        nivel_actual = 1
        
        while len(cola) > 0:
            print("Nivel ", nivel_actual, end=": ")
            num_nodos_nivel_actual = len(cola)
            
            for i in range(num_nodos_nivel_actual):
                nodo = cola.popleft()
                print(nodo.data, end=" ")
                
                if nodo.left is not None:
                    cola.append(nodo.left)
                
                if nodo.right is not None:
                    cola.append(nodo.right)
            
            print()
            nivel_actual += 1



arbol = Tree()  

texto = "muercielago"
for i in texto:
    arbol.insert(i)

'''
arbol.insert(15)
arbol.insert(25)
arbol.insert(10)
arbol.insert(7)
arbol.insert(22)
arbol.insert(17)
arbol.insert(13)
arbol.insert(5)
arbol.insert(9)
arbol.insert(27)
'''
print()
print("\nPreOrder:" )
arbol.preorder(arbol.root)
print("\ninOrder:")
arbol.inorder(arbol.root)
print("\nposOrder:")
arbol.postorder(arbol.root)

print("\n")
print("Niveles: ", arbol.maxDepth(arbol.root))

print("---Niveles---")
Niveles = arbol.niveles_arbol()
print(Niveles)

print("Graficar Arbol")
arbol.graficarArbol(arbol.root)



'''
print("\n")
arbol.imprimirAnchura(arbol.root, 0)

print("Árbol por nivel:")
arbol.nivel()
print()

print("")
print(arbol.levelorder(arbol.root))

'''