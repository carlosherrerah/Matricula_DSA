# c:\> pip install networkx
import numpy as np
import networkx as nx 
import matplotlib.pyplot as plt


# EJEMPLO DE LISTA DE ADYACENCIA
import numpy as np
graph = {"A": ["B", "C"],
         "B": ["A", "C", "D"],
         "C": ["A", "B", "D", "E"],
         "D": ["B", "C", "E", "F"],
         "E": ["C", "D"],
         "F": ["D"]}

# EJEMPLO DE MATRIZ DE ADYACENCIA
graph = np.array([[0, 1, 1, 0, 0, 0],
                  [1, 0, 1, 1, 0, 0],
                  [1, 1, 0, 1, 1, 0],
                  [0, 1, 1, 0, 1, 1],
                  [0, 0, 1, 1, 0, 0],
                  [0, 0, 0, 1, 0, 0]])

# EJEMPLO DE USO DE NETWORKX 
# Crear grafo vacío 
graph = nx.Graph() 

# Agregar nodos 
graph.add_node("A") 
graph.add_node("B") 
graph.add_node("C") 
graph.add_node("D") 
graph.add_node("E") 
graph.add_node("F")

# Agregar aristas 
graph.add_edge("A", "B") 
graph.add_edge("A", "C") 
graph.add_edge("B", "C") 
graph.add_edge("B", "D") 
graph.add_edge("C", "D") 
graph.add_edge("C", "E") 
graph.add_edge("D", "E") 
graph.add_edge("D", "F")

# Visualizar grafo 
nx.draw(graph, with_labels=True) 
plt.show() 

# Obtener métricas de grafo 
print("Número de nodos:", graph.number_of_nodes()) 
print("Número de aristas:", graph.number_of_edges()) 
print("Radio:", nx.radius(graph))
print("Diámetro:", nx.diameter(graph))

