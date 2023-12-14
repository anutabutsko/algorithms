"""
Theorem
Suppose G = (V , E) is a flow network and f is a flow. The following are equivalent:
f is a maximum flow in G.
The residual network has no augmenting path.
|f| = C (S, T) for some cut (S, T) of G.

Runtime using a DFS: O(Ef), where E is the number of edges and f is the maximum flow.
Runtime using a BFS: O(VE^2), where V is the number of vertices.
"""


def bfs(graph, source, sink, parent):
    visited = [False] * len(graph)
    queue = [source]
    visited[source] = True

    while queue:
        u = queue.pop(0)
        for ind, val in enumerate(graph[u]):
            if not visited[ind] and val > 0:
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u

    return visited[sink]


def ford_fulkerson(graph, source, sink):
    parent = [-1] * (len(graph))
    max_flow = 0

    while bfs(graph, source, sink, parent):
        path_flow = float("Inf")
        s = sink
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]

        max_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]

    return max_flow


matrix = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
          [4, 0, 8, 0, 0, 0, 0, 11, 0],
          [0, 8, 0, 7, 0, 4, 0, 0, 2],
          [0, 0, 7, 0, 9, 14, 0, 0, 0],
          [0, 0, 0, 9, 0, 10, 0, 0, 0],
          [0, 0, 4, 14, 10, 0, 2, 0, 0],
          [0, 0, 0, 0, 0, 2, 0, 1, 6],
          [8, 11, 0, 0, 0, 0, 1, 0, 7],
          [0, 0, 2, 0, 0, 0, 6, 7, 0]]

print(ford_fulkerson(matrix, 0, 5))
