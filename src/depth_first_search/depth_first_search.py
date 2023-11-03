from graph import generate_graph

import numpy as np


# Generate a random graph
graph = generate_graph()

# Check if graph is symmetric
if (graph == graph.transpose()).all():
    vertices = len(graph)
    edges = np.count_nonzero(graph) // 2
    print(f'Graph is symmetric and had {vertices} vertices and {edges} edges.')
