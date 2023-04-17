class Node:
    def __init__(self, val):
        self.left = None # apuntan a los nodos secundarios izquierdos
        self.right = None #apuntan a los nodos secundarios derechos 
        self.val = val #almacena el valor del nodo
        
def insert(root, val): #se toman el root y el val para insertar el arbol
    if root is None: #si root es none devuelve un nuevo nodo con el valor de val 
        return Node(val) #demuer lo contrario se inserta en el subárbol izquierdo
    if val < root.val: #si val es menor que el valor del nodo actual o en el subarbol derecho 
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

def traverse_inorder(root): #esta funcion realiza un recorrido en orden del arbol 
    if root is not None:
        traverse_inorder(root.left) #primero recorre el subarbol izquierdo luego el nodo raíz
        print(root.val, end=' ') #imprime el valor del nodo actual
        traverse_inorder(root.right) #despues recorre el subarbol derecho 
        
def traverse_preorder(root): #esta funcion realiza un recorrido de preorden del arbol 
    if root is not None:  
        print(root.val, end=' ') #imprimer el valor del nodo actual 
        traverse_preorder(root.left) #luego el subarbol izquierdo
        traverse_preorder(root.right) #luego el subarbol derecho

def traverse_postorder(root): #esta funcion realiza un recorrido posterior al orden del arbol
    if root is not None: 
        traverse_postorder(root.left) #primero se visita el subarbol izquierdo
        traverse_postorder(root.right) #luego el subarbol derecho 
        print(root.val, end=' ') #imprime el valor del nodo actual 
        
def print_tree_levels(root): #esta funcion imprime los niveles del arbol comenzando desde el nodo raiz
    queue = []               #donde utiliza una cola para recorrer el arbol en sentido amplio y almacenar los nodos en cada nivel en una lista 
    levels = []
    if not root:
        return
    queue.append(root)
    while queue:
        level = []
        for i in range(len(queue)):
            node = queue.pop(0)
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        levels.append(level)
    print(levels) #imprime la lista de niveles 

word = input("Enter a word: ") #se solicita al usuario ingresar una palabra 
root = Node(word[0]) #inicializa el root nodo con el primer caracter de la palabra
for i in range(1, len(word)): #repite varias veces el proceso sobre los caracteres restantes
    insert(root, word[i]) #los inserta en el arbol usando la funcion insert
    
print("Infix order: ", end='') #imprime el orden infijo 
traverse_inorder(root) #llama ala funcion que atraviesa el orden binario en orden infijo(iz,n,d)
print()

print("Prefix order: ", end='') #imprime el orden de prefijo
traverse_preorder(root) #llama ala funcion que atraviesa el orden binario en orden prefijo(n,iz,d)
print()

print("Postfix order: ", end='')
traverse_postorder(root) #llama ala funcion que atraviesa el orden binario en orden postfijo(iz,d,n)
print()

print("Tree levels: ") #funcion que imprime los nodos del arbol binario nivel por nivel comenzando desde la raiz
print_tree_levels(root)
