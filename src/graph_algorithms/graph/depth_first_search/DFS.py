def DFS(graph, start):
    n = len(graph)
    visited = [False] * n

    stack = []

    explore(start, visited, stack, graph, n)

    return stack


def explore(node, visited, stack, graph, n):
    visited[node] = True

    stack.append(node)

    for i in range(n):
        if graph[node][i] > 0 and not visited[i]:
            explore(i, visited, stack, graph, n)


matrix = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
          [4, 0, 8, 0, 0, 0, 0, 11, 0],
          [0, 8, 0, 7, 0, 4, 0, 0, 2],
          [0, 0, 7, 0, 9, 14, 0, 0, 0],
          [0, 0, 0, 9, 0, 10, 0, 0, 0],
          [0, 0, 4, 14, 10, 0, 2, 0, 0],
          [0, 0, 0, 0, 0, 2, 0, 1, 6],
          [8, 11, 0, 0, 0, 0, 1, 0, 7],
          [0, 0, 2, 0, 0, 0, 6, 7, 0]]

print(DFS(matrix, 0))


"""
Runtime for DFS is O(|V| + |E|).

A directed graph is acyclic if and only if the DFS edge classification contains no back edges.

A topological sort of a DAG is a linear ordering of the vertices such that if G contains an 
edge (u, v) then u appears in the ordering before v .
Only DAGs have topological ordering.

Topological sort runs in O(|V| + |E|) time.
"""
