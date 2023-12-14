def prims(graph, start):
    n = len(graph)
    visited = [False] * n
    visited[start] = True
    result = []

    counter = 0

    while counter < n - 1:
        min_weight = float('inf')
        for i in range(n):
            if visited[i]:
                for j in range(n):
                    if not visited[j] and graph[i][j]:
                        if min_weight > graph[i][j]:
                            min_weight = graph[i][j]
                            s = i
                            d = j

        result.append([s, d, graph[s][d]])
        visited[d] = True
        counter += 1

    return result


matrix = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
          [4, 0, 8, 0, 0, 0, 0, 11, 0],
          [0, 8, 0, 7, 0, 4, 0, 0, 2],
          [0, 0, 7, 0, 9, 14, 0, 0, 0],
          [0, 0, 0, 9, 0, 10, 0, 0, 0],
          [0, 0, 4, 14, 10, 0, 2, 0, 0],
          [0, 0, 0, 0, 0, 2, 0, 1, 6],
          [8, 11, 0, 0, 0, 0, 1, 0, 7],
          [0, 0, 2, 0, 0, 0, 6, 7, 0]]


start = 0
result = prims(matrix, 0)

for v, u, w in result:
    print(f'{v} -> {u}, weight: {w}')

"""
Prims algorithm is a greedy algorithm used to find a minimum spanning tree for 
a weighted undirected graph.
Runtime: O(|E|log(|V|))
"""
