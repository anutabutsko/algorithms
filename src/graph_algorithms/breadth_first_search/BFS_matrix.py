"""
A natural approach to starting such an investigation is to begin by
first exploring all nodes directly connected to source by an edge.
Having completed this task, consider studying all nodes connected
by two edges to source and repeat.
This ”shelling” can be formalized and goes by the name of breadth
first search.

The runtime of BFS is O(|V| + |E|)
"""


def BFS(graph, start):
    n = len(graph)

    queue = [start]
    result = []

    while queue:
        current = queue.pop(0)
        result.append(current)
        for i in range(n):
            if graph[current][i] > 0:
                if i not in result and i not in queue:
                    queue.append(i)

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


print(BFS(matrix, 0))
