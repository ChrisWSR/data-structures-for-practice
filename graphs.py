# simple graph
# how we represent a graph in python
# adjencency list
# matrix and agencency matrix

import matplotlib.pyplot as plt
import networkx as nx
from collections import deque
def draw_graph(graph, title="Visualización del Grafo", 
               node_color='lightblue', node_size=1500, 
               edge_color='gray', figsize=(12, 8), 
               save_to=None):
    """Dibuja un grafo usando NetworkX y Matplotlib"""
    G_visual = nx.Graph(graph.adjacency_list)
    plt.figure(figsize=figsize)
    pos = nx.spring_layout(G_visual, k=2, iterations=50)
    
    nx.draw(G_visual, pos, 
            with_labels=True,
            node_color=node_color,
            node_size=node_size,
            font_size=16,
            font_weight='bold',
            edge_color=edge_color,
            width=2)
    
    plt.title(title, fontsize=20)
    plt.axis('off')
    plt.tight_layout()
    
    if save_to:
        plt.savefig(save_to, dpi=300, bbox_inches='tight')
        print(f"✓ Guardado en: {save_to}")
    
    plt.show()



class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self,vertex):
        if vertex in self.adjacency_list:
            raise Exception("Vertex already  in graph")
        self.adjacency_list[vertex] = []
        return self
    def add_edge(self,vertex1, vertex2):
        if vertex1 not in self.adjacency_list or vertex2 not in self.adjacency_list:
            raise Exception("Invalid vertices")
        self.adjacency_list[vertex1].append(vertex2)
        self.adjacency_list[vertex2].append(vertex1)
        return self
    
    def remove_edge(self,vertex1, vertex2):
        if vertex1 not in self.adjacency_list or vertex2 not in self.adjacency_list:
            raise Exception("Invalid vertices")
        self.adjacency_list[vertex1].remove(vertex2)
        self.adjacency_list[vertex2].remove(vertex1)
        return self
    def remove_vertex(self,vertex):
        if vertex not in self.adjacency_list:
            raise Exception("Vertex not in graph")
        for neighbor in self.adjacency_list[vertex]:
            self.adjacency_list[neighbor].remove(vertex)
        self.adjacency_list.pop(vertex)
        return self
    def breadth_fist_transversal(self,start):
        if start not in self.adjacency_list:
            raise Exception("Vertex not in graph")
        queue = deque()
        queue.append(start)
        visited = []
        explored = {vertex: False for vertex in self.adjacency_list}
        explored[start] = True
        while queue:
            current = queue.popleft()
            visited.append(current)
            for adjacent in self.adjacency_list[current]:
                if not explored[adjacent]:
                    queue.append(adjacent)
                    explored[adjacent] = True
        return visited

    def dft_iterative(self,start):
        if start not in self.adjacency_list:
            raise Exception("Vertex not in graph")
        stack = [start]
        visited = []
        explored = {vertex: False for vertex in self.adjacency_list}
        explored[start] = True
        while stack:
            current = stack.pop()
            visited.append(current)
            for adjacent in self.adjacency_list[current]:
                if not explored[adjacent]:
                    stack.append(adjacent)
                    explored[adjacent] = True
        return visited
    def dft_recursive(self,start):
        if start not in self.adjacency_list:
            raise Exception("Vertex not in graph")
        visited = []
        explored = {vertex: False for vertex in self.adjacency_list}

        def _traverse(current):
            visited.append(current)
            explored[current] = True
            for adjacent in self.adjacency_list[current]:
                if not explored[adjacent]:
                    _traverse(adjacent)
            return
        _traverse(start)
        return visited

G1 = Graph()

vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
for vertex in vertices:
    G1.add_vertex(vertex)

# 2. Agregar todas las aristas (solo una vez por par)
edges = [
    ('A', 'B'), ('A', 'C'), ('A', 'D'),
    ('B', 'C'),
    ('C', 'D'), ('C', 'J'),
    ('D', 'E'), ('D', 'I'),
    ('E', 'F'), ('E', 'G'), ('E', 'I'),
    ('F', 'H'),
    ('G', 'H'), ('G', 'K'),
    ('H', 'J'), ('H', 'K'),
    ('I', 'J'),
    ('J', 'K')
]

for v1, v2 in edges:
    G1.add_edge(v1, v2)

# Verificar el resultado
print(G1.adjacency_list)
print("visited nodes on G1 graph",G1.breadth_fist_transversal('E'))
print("visited nodes on G1 graph",G1.dft_iterative('E'))
print("visited nodes on G1 graph",G1.dft_recursive('E'))

#draw_graph(G1)
#G1.remove_edge('F','H')
#draw_graph(G1)
#G1.remove_vertex('J')
#draw_graph(G1)

