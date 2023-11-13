import random
from time import perf_counter

import numpy as np


def generate_graph(seed=None, n=10, start=1, end=4):
    if seed:
        random.seed(seed)
    N = n
    a = np.random.randint(start, end, (N, N))
    A = (a + a.T)
    for i in range(N):
        A[i, i] = 0
    b = np.random.randint(start, end, size=(N, N))
    B = (b + b.T)
    for i in range(N):
        B[i, i] = 0
    c = np.random.randint(start, end, size=(N, N))
    C = (c + c.T)
    for i in range(N):
        C[i, i] = 0
    Z = np.zeros((N, N), dtype=int)
    R1 = np.block([np.block([A, Z]), Z])
    R2 = np.block([np.block([Z, B]), Z])
    R3 = np.block([np.block([Z, Z]), C])
    P = np.zeros((3 * N, 3 * N), dtype=int)
    for i in range(2):
        for j in range(1, 3):
            P[8 + j - 1, (i + 1) * N + j] = 1
    P = (P + P.T)
    M = np.block([np.block([R1.T, R2.T]), R3.T]) + P

    return M


# Check if the graph is connected.
def is_connected(graph):
    n = len(graph)
    for i in range(n):
        flag = False
        if graph[0][i] == 0:
            for j in range(n):
                if graph[j][i] != 0:
                    flag = True
                    break
            # If no connection is found, the graph is not connected.
            if not flag:
                return False
    # If connections are found for all nodes, the graph is connected.
    return True


# Returns a list of source, destination and weight for each edge.
def sort_by_weight(graph):
    edge_list = []
    # Keep track of visited edges.
    visited = set()
    n = len(graph)
    for i in range(n):
        for j in range(n):
            # Add edge if it's not a duplicate and the weight is non-zero.
            if graph[i][j] != 0 and (j, i) not in visited:
                edge_list.append([i, j, graph[i][j]])
                visited.add((i, j))

    # Return the edge list sorted by weight.
    return sorted(edge_list, key=lambda x: x[2])


# Find the root of the set that the item belongs to.
def find(visited, item):
    if visited[item][0] == item:
        return item
    # Recursively find the root.
    return find(visited, visited[item][0])


# Perform the union operation.
def union(visited, x, y):
    # Find the roots of the sets x and y belong to.
    x_root = find(visited, x)
    y_root = find(visited, y)
    # Perform the union operation based on rank.
    if visited[x_root][1] < visited[y_root][1]:
        visited[x_root][0] = y_root
    elif visited[x_root][1] > visited[y_root][1]:
        visited[y_root][0] = x_root
    else:
        # If ranks are equal, make one as root and increase its rank.
        visited[y_root][0] = x_root
        visited[x_root][1] += 1


# Implement Kruskal's Algorithm
def kruskalsAlgorithm(graph):
    # Sort the edges of the graph by weight.
    edge_list = sort_by_weight(graph)
    # Initialize sets with parents and ranks for each vertex.
    visited = [[vertex, 0] for vertex in range(len(graph))]
    result = []

    for edge in edge_list:
        s, d, w = edge
        # Find roots of the sets the vertices belong to.
        x = find(visited, s)
        y = find(visited, d)
        # If roots are different, add the edge to the result and union the sets.
        if x != y:
            result.append(edge)
            union(visited, x, y)
        # Stop when a minimum spanning tree is formed.
        if len(result) == len(graph) - 1:
            break

    return result


# Calculate the Runtime.
def compute_runtime(runs, size):
    total_time = 0

    for _ in range(runs):
        graph = generate_graph(n=size)

        # Start timer.
        start = perf_counter()
        # Run DFS on the generated graph.
        kruskalsAlgorithm(graph)
        # Stop timer.
        stop = perf_counter()
        # Calculate the time for this run.
        time = stop - start
        # Accumulate the total time.
        total_time += time

    # Compute the average time by dividing the total time by the number of runs.
    average_time = total_time / runs

    return average_time


# Find n largest unique weights.
def find_largest_weights(graph, n):
    # Sort the edges of the graph by weight.
    edge_list = sort_by_weight(graph)
    weights = []
    start = -1  # Starting from the largest weight.

    # Ensure not to exceed the number of unique weights.
    while len(weights) < n and -start <= len(edge_list):
        # Check if the current weight is already in the list.
        if edge_list[start][2] not in weights:
            weights.append(edge_list[start][2])
        start -= 1  # Move to the next largest weight.

    # Return the n largest unique weights.
    return weights
