from matplotlib import pyplot as plt

from kruskals_algorithm import *

# Generate graph.
graph = generate_graph(seed=123)

# Check if the graph is connected
if is_connected(graph):
    print('Graph is connected.')
else:
    print('Graph is not connected.')

# Kruskal's Algorithm
print("\nMinimum Spanning Tree's Edges:")
for edge in kruskalsAlgorithm(graph):
    print(f"{edge[0]} -> {edge[1]}, weight {edge[2]}")

# # Increasing N.
sizes = [i for i in range(10, 300, 10)]
times = []

for size in sizes:
    times.append(compute_runtime(runs=10, size=size))

plt.plot(sizes, times)
plt.xlabel('Size of the graph.')
plt.ylabel('Time')
plt.title("Kruskal's Algorithm Runtime")

plt.grid(True)

plt.show()

# Three largest weights in the graph.
print("\nThree Largest Weights in the Graph:")
print(*find_largest_weights(graph, 3), sep=', ')

# Return three edges with the largest weights from MST.
print("\nThree Edges with Largest Weights from MST:")
edges = kruskalsAlgorithm(graph)
for i in range(-1, -4, -1):
    print(f"{edges[i][0]} -> {edges[i][1]}, weight {edges[i][2]}")

"""
The runtime of MST-Kruskal is O(|E|log(|E|)).
"""
