import numpy as np


def adj_mat(info, n):
    graph = [[0] * n for _ in range(n)]

    for v, u, w in info:
        graph[v][u] = w

    return graph


def adj_mat_numpy(info, n):
    graph = np.zeros((n, n))

    for v, u, w in info:
        graph[v][u] = w

    return graph


flights = [(0, 1, 100), (1, 2, 200), (0, 2, 300)]
n_airports = 3

print(adj_mat(flights, n_airports))
print(adj_mat_numpy(flights, n_airports))
