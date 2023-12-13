def dijkstra(graph, src):
    n = len(graph)

    visited = []
    distances = {i: [float('inf'), []] for i in range(n)}
    distances[src][0] = 0

    for _ in range(n):
        # select the unvisited node with the smallest distance
        minimum_value = float('inf')
        for i in range(n):
            if i not in visited and distances[i][0] < minimum_value:
                minimum_value = distances[i][0]
                u = i

        visited.append(u)

        # update the distance
        for v in range(n):
            if graph[u][v] > 0 and v not in visited:
                if distances[v][0] > distances[u][0] + graph[u][v]:
                    distances[v][0] = distances[u][0] + graph[u][v]
                    distances[v][1] = distances[u][1] + [str(u)]

    return distances


Graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
         [4, 0, 8, 0, 0, 0, 0, 11, 0],
         [0, 8, 0, 7, 0, 4, 0, 0, 2],
         [0, 0, 7, 0, 9, 14, 0, 0, 0],
         [0, 0, 0, 9, 0, 10, 0, 0, 0],
         [0, 0, 4, 14, 10, 0, 2, 0, 0],
         [0, 0, 0, 0, 0, 2, 0, 1, 6],
         [8, 11, 0, 0, 0, 0, 1, 0, 7],
         [0, 0, 2, 0, 0, 0, 6, 7, 0]]


start = 0
result = dijkstra(Graph, start)

for key, value in result.items():
    print(f"Minimum distance from node {start} to node {key} is {value[0]}.")
    if value[0]:
        print(f"Path: {' -> '.join(value[1])} -> {key}")

"""
For greedy algorithm to work, the problem should exhibit:
Optimal substructure
Overlapping subproblems
Once we have checked that the above hold, the problem should exhibit the greedy choice property:
We can assemble an optimal solution by making locally optimal choices.
"""
