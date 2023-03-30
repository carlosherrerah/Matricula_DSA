from anytree import Node, RenderTree

class Nodo:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def preorder(node):
    if node:
        print(node.data)
        preorder(node.left)
        preorder(node.right)   


root = Nodo(10)

root.left = Nodo(34)
root.right = Nodo(89)
root.left.left = Nodo(45)
root.left.right = Nodo(50)

preorder(root)

'''
root = Node(10)

level_1_child_1 = Node(34, parent=root)
level_1_child_2 = Node(89, parent=root)
level_2_child_1 = Node(45, parent=level_1_child_1)
level_2_child_2 = Node(50, parent=level_1_child_2)
'''
for pre, fill, node in RenderTree(root):
    print("%s%s" % (pre, node.name))

 

