import numpy as np


np.random.seed(123)

A = []
N = 50
c1 = 5
e = 7


for i in range(N):
    for j in range(c1):
        for k in range(c1):
            T1 = np.random.randint(1, c1+1)
            if T1 > 1:
                A.append([c1*i+j, c1*(i+1) + k, np.random.randint(1, e)])


num_edges = len(A)
print(f"Number of edges: {num_edges}")

num_vertices = []
for u, v, w in A:
    if u not in num_vertices:
        num_vertices.append(u)

print(f"Number of vertices: {len(num_vertices)}")


"""
Answers:
a)
i.: 999
ii.: 250

b)
i.: To check whether the graph is connected we can use either DFS or BFS algorithms. 

The runtime of BFS is O(|V| + |E|).

Runtime for DFS is O(|V| + |E|).

ii.: To check whether the graph is a DAG we can run a topological sort on it.
A directed graph is acyclic if and only if this can be done.

Runtime: O(V + E). 

Another way to check for a DAG is to run a DFS on the graph. A graph is a DAG if DFS finds no back edges.

iii.: Bellman-Ford algorithm.
Provides shortest path from one node to all nodes, however, unlike with other shortest path algorithms: negative edges allowed.
Theorem: Bellman-Ford will stabilize in |V| − 1 iterations of the external FOR-loop if and only if there are no negative cycles.
If the algorithm doesn't stabilize after |V| − 1 iterations, we can conclude that negative cycle(s) are presents in the graph.

The runtime for Bellman-Ford is O(|V||E|)

iv.: Floyd-Warshall algorithm.
Provides the distance between all pair of vertices. Negative edges allowed.

Runtime: O(V^3)

c) To distinguish between Bellman-Ford and Dijkstra or any DAG algorithm, I would change some of the weights in the 
graph to negative and see if algorithm will work. It will only work if the algorithm that professor X implemented
is Bellman-Ford.
If the algorithm crashed, then we are left with two other possible solutions: Dijkstra or shortest path via topological
sort. Since topological sort only works on DAGs, I would adjust the graph to add a cycle and see if the algorithm works.
If it worked, then the answer is Dijkstra, since it can still work on graphs with cycles. If the algorithm crashes, then
the answer is shortest path via topological sort algorithm.
"""