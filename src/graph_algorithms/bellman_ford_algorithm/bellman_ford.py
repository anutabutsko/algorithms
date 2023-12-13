# Import initialize_graph function from graphs.py file
from graphs import initialize_graph


# Define a Graph class
class Graph:
    def __init__(self):
        self.vertices = []  # Initialize an empty list to store vertices
        self.edges = []  # Initialize an empty list to store edges

    # Method to add an edge to the graph
    def add_edge(self, vertex, edge, weight):
        self.edges.append([vertex, edge, weight])

    # Method to add a vertex to the graph
    def add_vertex(self, vertex):
        self.vertices.append(vertex)

    # Method to print the result
    @staticmethod
    def print_result(distances, source):
        for destination, distance in distances.items():
            if type(distance[0]) is int:
                print(f'Shortest distance from node {source} to node {destination} is {distance[0]}.\n'
                      f'Path: {distance[1] + str(destination)}')
            else:
                print(f'Path from node {source} to node {destination} does not exist.')

    # bellman_ford_algorithm
    def BellmanFord(self, source):
        # Initialize distances dictionary with initial values of all edges as Infinity and an empty string to save the path
        distances = {i: [float("Inf"), ""] for i in self.vertices}

        # Initialize the source vertex value as 0
        distances[source][0] = 0

        # Iterate through the graph vertices
        for _ in range(len(self.vertices) - 1):
            # Iterate through each edge in the graph
            for vertex, edge, weight in self.edges:
                # Check if the distance to the vertex is not infinity and if the distance
                # from that vertex to the edge is shorter than the current known distance to that edge
                if distances[vertex][0] != float("Inf") and distances[vertex][0] + weight < distances[edge][0]:
                    # Update distance to the edge if the distance from the vertex is shorter than existing distance
                    distances[edge][0] = distances[vertex][0] + weight
                    # Update the path from source vertex to current vertex
                    distances[edge][1] = (distances[vertex][1] + str(vertex) + ' -> ')

        # Call the print_result method to display the results
        self.print_result(distances, source)


# Create an instance of the Graph class
g = Graph()

# Initialize the graph payload using the initialize_graph function
payload = initialize_graph()

# Add nodes to the graph
for vertex in range(21):
    g.add_vertex(vertex)

# Add edges to the graph
for edge in payload:
    vertex, edge, weight = edge
    g.add_edge(vertex, edge, weight)

# Run the bellman_ford_algorithm that finds the path from vertex 0 to every edge
g.BellmanFord(0)

"""
Output: 
Shortest distance from node 0 to node 0 is 0.
Path: 0
Shortest distance from node 0 to node 1 is 3.
Path: 0 -> 1
Shortest distance from node 0 to node 2 is 3.
Path: 0 -> 2
Shortest distance from node 0 to node 3 is 7.
Path: 0 -> 3
Shortest distance from node 0 to node 4 is 2.
Path: 0 -> 4
Shortest distance from node 0 to node 5 is 4.
Path: 0 -> 5
Path from node 0 to node 6 does not exist.
Path from node 0 to node 7 does not exist.
Path from node 0 to node 8 does not exist.
Path from node 0 to node 9 does not exist.
Path from node 0 to node 10 does not exist.
Shortest distance from node 0 to node 11 is 10.
Path: 0 -> 4 -> 11
Shortest distance from node 0 to node 12 is 5.
Path: 0 -> 4 -> 12
Shortest distance from node 0 to node 13 is 4.
Path: 0 -> 1 -> 13
Shortest distance from node 0 to node 14 is 4.
Path: 0 -> 1 -> 14
Shortest distance from node 0 to node 15 is 12.
Path: 0 -> 4 -> 12 -> 15
Shortest distance from node 0 to node 16 is 6.
Path: 0 -> 1 -> 14 -> 16
Shortest distance from node 0 to node 17 is 6.
Path: 0 -> 1 -> 13 -> 17
Shortest distance from node 0 to node 18 is 8.
Path: 0 -> 4 -> 12 -> 18
Shortest distance from node 0 to node 19 is 5.
Path: 0 -> 1 -> 13 -> 19
Shortest distance from node 0 to node 20 is 9.
Path: 0 -> 1 -> 14 -> 16 -> 20
"""

"""
For initialization:

import math
V = [0,1,2,3,4,5,6]
E = [[0,1,3], [0,2,2], [0,3,1], [1,4,5], [2,1,1],
[2,4,3], [2,3,1], [2,5,4], [3,5,7], [4,6,5], [5,6,8]]
INF = math.inf
d = [0]
for i in range(0,len(V)-1):
    d.append(INF)
print(’Initialization is ’,d)
"""

"""
The Bellman-Ford algorithm is a graph algorithm used to find the shortest paths from a single source vertex 
to all other vertices in a weighted graph. Here's a short description of how it works:
1. Initialization: First, the distances to all vertices are set to infinity, except for the source vertex, 
which is set to zero.
2. Relaxation: The algorithm then iteratively relaxes edges in the graph. Relaxation means that for each 
edge, the algorithm checks if the shortest path to the destination vertex of the edge can be improved by 
going through the source vertex of the edge. If it can, the distance to the destination vertex is updated.
3. Iteration: This process of relaxation is repeated for all edges in the graph. In the Bellman-Ford 
algorithm, this relaxation step is repeated ( V - 1 ) times, where ( V ) is the number of vertices 
in the graph. This ensures that the shortest path to each vertex, if it exists, is correctly calculated.
4. Negative Cycle Detection: After the ( V - 1 ) iterations, the algorithm checks for negative weight 
cycles in the graph by performing one more iteration of relaxation. If the distance to any vertex is 
updated in this iteration, it means there is a negative weight cycle in the graph. Since paths in such 
a cycle can be reduced indefinitely, the shortest path is not well-defined.

The Bellman-Ford algorithm is especially useful in graphs where edges can have negative weights, unlike 
algorithms like Dijkstra's, which only work with non-negative edge weights. However, it's less efficient 
than Dijkstra's for graphs without negative weight edges due to its higher time complexity.

The runtime for Bellman-Ford is O(|V||E|)

Theorem
Bellman-Ford will stabilize in |V| − 1 iterations of the external FOR-loop if and only if there are 
no negative cycles.
"""