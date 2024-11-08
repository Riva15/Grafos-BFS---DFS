import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

def draw_graph(graph, pos, visited=None, current_node=None, title="Grafo"):
    plt.figure(figsize=(8, 6))
    nx.draw(graph, pos, with_labels=True, node_color=['lightblue' if node not in (visited or []) else 'orange' for node in graph.nodes()],
            edge_color='gray', node_size=800, font_size=10, font_color='black')
    if current_node is not None:
        nx.draw_networkx_nodes(graph, pos, nodelist=[current_node], node_color='red', node_size=800)
    plt.title(title)
    plt.show()

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    pos = nx.spring_layout(graph)

    while queue:
        current = queue.popleft()
        if current not in visited:
            visited.add(current)
            draw_graph(graph, pos, visited=visited, current_node=current, title=f"BFS Visitando: {current}")
            for neighbor in graph.neighbors(current):
                if neighbor not in visited:
                    queue.append(neighbor)
    print("BFS - Nodos visitados en orden:", visited)

def dfs(graph, start, visited=None, pos=None):
    if visited is None:
        visited = set()
        pos = nx.spring_layout(graph)

    visited.add(start)
    draw_graph(graph, pos, visited=visited, current_node=start, title=f"DFS Visitando: {start}")
    for neighbor in graph.neighbors(start):
        if neighbor not in visited:
            dfs(graph, neighbor, visited=visited, pos=pos)
    return visited

# Crear el grafo de ejemplo
G = nx.Graph()
edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'F'), ('C', 'G')]
G.add_edges_from(edges)

# Visualizar BFS
print("Ejecutando BFS:")
bfs(G, 'A')

# Visualizar DFS
print("\nEjecutando DFS:")
dfs(G, 'A')
