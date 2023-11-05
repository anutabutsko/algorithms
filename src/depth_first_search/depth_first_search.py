from graph import generate_graph

import numpy as np


def DFS(graph):
    graph_dict = {}
    seen = []
    for vertex in range(len(graph)):
        graph_dict[vertex] = []
        seen.append(vertex)
        for connection in range(len(graph[vertex])):
            if graph[vertex][connection] > 0 and connection not in seen:
                graph_dict[vertex].append(connection)

    visited = set()
    stk = []
    for vertex in graph_dict:
        if vertex in visited:
            continue

        while vertex is not None:
            flag = False
            visited.add(vertex)
            if graph_dict[vertex]:
                for connection in graph_dict[vertex]:
                    if connection not in visited:
                        stk.append(vertex)
                        vertex = connection
                        flag = True
                        break

            if not flag:
                if stk:
                    vertex = stk.pop()
                else:
                    vertex = None

    return visited


# Generate a random graph
graph = generate_graph()

# Q1 How many vertices in the graph?  How many edges?

# Check if graph is symmetric
if (graph == graph.transpose()).all():
    vertices = len(graph)
    edges = np.count_nonzero(graph) // 2
    print(f'Graph is symmetric and has {vertices} vertices and {edges} edges.')

print(DFS(graph))

