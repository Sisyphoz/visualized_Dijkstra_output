from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt

nodes_and_distances = {
    'a': {'b': 2, 'c': 3, 'w': 33},
    'b': {'d': 9, 'e': 8, 'f': 5},
    'c': {'k': 8},
    'd': {'l': 11, 'm': 7, 'n': 12},
    'e': {'h': 12},
    'g': {'i': 4},
    'k': {'p': 6, 'q': 1},
    'h': {'w': 6},
    'q': {'y': 16},
    'p': {'q': 1},
    'w': {'y': 4},
}

def dijkstra(graph, start, end):
    distances = defaultdict(lambda: float('inf'))
    previous = defaultdict(lambda: None)
    distances[start] = 0
    unvisited = set(graph.keys())
    while unvisited:
        current = min(unvisited, key=lambda x: distances[x])
        unvisited.remove(current)

        if distances[current] == float('inf'):
            break
        for neighbor, distance in graph[current].items():
            alt = distances[current] + distance
            if alt < distances[neighbor]:
                distances[neighbor] = alt
                previous[neighbor] = current

    path = []
    current = end
    while current:
        path.append(current)
        current = previous[current]

    return list(reversed(path)), distances[end]

# Create a graph using the nodes and distances dictionary
graph = nx.Graph()
for node, neighbors in nodes_and_distances.items():
    for neighbor, distance in neighbors.items():
        graph.add_edge(node, neighbor, weight=distance)

start = 'a'
end = 'k'

# Use the dijkstra algorithm to find the shortest path:
# path, distance = dijkstra(nodes_and_distances, start, end)
# to use hand made solution, or alternatively:
path = nx.dijkstra_path(graph, start, end)
distance = nx.dijkstra_path_length(graph, start, end)

# Create a graph using the nodes and distances dictionary
graph = nx.Graph()
for node, neighbors in nodes_and_distances.items():
    for neighbor, distance in neighbors.items():
        graph.add_edge(node, neighbor, weight=distance)

# Create a list of edges for the shortest path
edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]

# Draw the graph and the shortest path
pos = nx.spring_layout(graph)
nx.draw_networkx(graph, pos)
nx.draw_networkx_edges(graph, pos, edgelist=edges, width=8, alpha=0.5, edge_color='r')
nx.draw_networkx_labels(graph, pos)

# Show the plot and text output.
print(f"Shortest path from {start} to {end}: {path} (total distance: {distance})")
plt.show()



# The time complexity of the Dijkstra algorithm, represented by the function dijkstra()
# is O(|E| + |V| log |V|), where |E| is the number of edges in the graph
# and |V| is the number of vertices (nodes) in the graph.

# In this case, the graph is represented using a dictionary of dictionaries,
# where each key represents a node and the corresponding value is a dictionary
# containing the neighboring nodes and the distances to them.
# The time complexity of the dijkstra() function depends on the number of
# edges and vertices in the graph.
#
# The dijkstra() function uses the min() function to find the node with the minimum
# distance from the start node. This operation has a time complexity of O(|V| log |V|),
# because it involves sorting the distances of all nodes in the graph.
# Also, the function iterates over all the edges in the graph, which has a time complexity
# of O(|E|). The overall time complexity of the dijkstra() function is O(|E| + |V| log |V|).
