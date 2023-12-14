"""
Provides the shortest path between all pair of vertices. Negative edges allowed.
Runtime: O(V^3)
Does not require a DAG.
"""


def floyd_warshall(graph):
    result = graph
    n = len(graph)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                result[i][j] = min(result[i][j], result[i][k] + result[k][j])

    return result


matrix = [[0, 4, float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 8, float('inf')],
          [4, 0, 8, float('inf'), float('inf'), float('inf'), float('inf'), 11, float('inf')],
          [float('inf'), 8, 0, 7, float('inf'), 4, float('inf'), float('inf'), 2],
          [float('inf'), float('inf'), 7, 0, 9, 14, float('inf'), float('inf'), float('inf')],
          [float('inf'), float('inf'), float('inf'), 9, 0, 10, float('inf'), float('inf'), float('inf')],
          [float('inf'), float('inf'), 4, 14, 10, 0, 2, float('inf'), float('inf')],
          [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 2, 0, 1, 6],
          [8, 11, float('inf'), float('inf'), float('inf'), float('inf'), 1, 0, 7],
          [float('inf'), float('inf'), 2, float('inf'), float('inf'), float('inf'), 6, 7, 0]]

print(floyd_warshall(matrix))
