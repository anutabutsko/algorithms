import sys
from time import perf_counter

import matplotlib.pyplot as plt
import numpy as np

from graph import generate_graph

sys.setrecursionlimit(10000)  # Set a higher recursion limit


# Function to convert an adjacency matrix to a dictionary representation of the graph.
def convert(graph):
    # Initialize an empty dictionary for the graph representation.
    graph_dict = {}
    # Iterate over each vertex in the graph.
    for vertex in range(len(graph)):
        # Initialize the vertex entry with an empty list of connections(vertices that the vertex is connected to).
        graph_dict[vertex] = {"connections": []}
        # Check for connections to other vertices.
        for connection in range(len(graph[vertex])):
            # If there's a positive entry in the adjacency matrix, it means there is a connection.
            if graph[vertex][connection] > 0:
                # Append the connection to the vertex's list of connections.
                graph_dict[vertex]["connections"].append(connection)

    return graph_dict


# Function to perform Depth First Search on the graph.
def DFS(graph):
    # Initialize time to track the discovery and finish times.
    time = [0]

    # Initialize a dictionary to track the greatest distance.
    greatest_distance = {'value': 0}

    # Initialize all vertices in the graph as unvisited, marking them with color "white".
    for vertex in graph:
        graph[vertex]["color"] = "white"
        graph[vertex]["previous"] = None

    # Iterate over each vertex in the graph.
    for vertex in graph:
        # If the vertex is unvisited, start the exploration process.
        if graph[vertex]["color"] == "white":
            current_distance = 0
            explore(graph, vertex, time, current_distance, greatest_distance)

    return graph, greatest_distance


# Function to explore the graph starting from a given vertex.
def explore(graph, vertex, time, current_distance, greatest_distance):
    # Increment the discovery time for this vertex.
    time[0] += 1
    graph[vertex]["discovery_time"] = time[0]

    # Mark this vertex as being visited.
    graph[vertex]["color"] = "gray"

    # Explore all connections for the current vertex.
    for connection in graph[vertex]["connections"]:
        # If the connected vertex is unvisited, recursively explore it.
        if graph[connection]["color"] == "white":
            graph[connection]["previous"] = vertex
            current_distance += 1  # Increment distance for this path.
            explore(graph, connection, time, current_distance, greatest_distance)

    # Once exploration is complete, mark the vertex as finished.
    graph[vertex]["color"] = "black"

    # Increment the finish time for this vertex.
    time[0] += 1
    graph[vertex]["finish_time"] = time[0]

    # Update the greatest distance if the current path is the longest.
    greatest_distance['value'] = max(greatest_distance['value'], current_distance)


# Check if the graph is connected.
def check_if_connected(graph):
    # Initialize a list to collect vertices that are not connected to any other vertices.
    not_connected = []

    # Iterate through the result of DFS to check for unvisited vertices.
    for vertex in graph:
        if not graph[vertex]["connections"]:
            # If a vertex is still white, it was not visited by DFS and is not connected.
            not_connected.append(vertex)

    # Check if there are any not connected vertices.
    if not_connected:
        return f"Vertices {', '.join(map(str, not_connected))} are not connected to the graph."
    else:
        return "The graph is fully connected."


# Compute average search time.
def compute_search_time(runs, n=None):
    total_time = 0

    for _ in range(runs):
        # Generate graph without setting seed value to ensure a new graph is generated every time.
        if n:
            # Adjust number N.
            graph = generate_graph(n=n)
        else:
            graph = generate_graph()

        # Convert the graph to a dictionary representation.
        graph = convert(graph)
        # Start timer.
        start = perf_counter()
        # Run DFS on the generated graph.
        DFS(graph)
        # Stop timer.
        stop = perf_counter()
        # Calculate the time for this run.
        time = stop - start
        # Accumulate the total time.
        total_time += time

    # Compute the average time by dividing the total time by the number of runs.
    average_time = total_time / runs

    return average_time


# MAIN SCRIPT

# Generate a random graph with seed 123.
graph = generate_graph(123)

# QUESTION 1: How many vertices in the graph? How many edges?
if (graph == graph.transpose()).all():
    vertices = len(graph)
    # Count the number of edges, considering symmetry.
    edges = np.count_nonzero(graph) // 2
    print(f'Graph is symmetric and has {vertices} vertices and {edges} edges.')

# QUESTION 2: Implement depth-first search. Is the underlying graph connected?
# How long does it take the search to run on average? (be precise concerning what you are measuring).

# Convert the graph to a dictionary representation.
graph_dict = convert(graph)

# Perform Depth First Search on the graph and print the result.
result, greatest_dist = DFS(graph_dict)
print(result)

# Check if the underlying graph is connected.
print(check_if_connected(result))

# Average search time over 10000 runs.
print(f"The average time taken for DFS search over 10000 runs is {round(compute_search_time(10000), 6):.6f} seconds.")

# QUESTION 3: What is the greatest distance between any two connected points in the graph?
print(f"The greatest distance between any two connected points in the graph is {greatest_dist['value']}.")

# QUESTION 5: Change the random integer calls in lines 16, 20 and 24 to draw either 0 or 1. Does the graph remain connected?
new_graph_1 = generate_graph(start=0, end=1)
# Convert the graph to a dictionary representation.
new_graph_dict = convert(new_graph_1)
new_result_1, greatest_dist = DFS(new_graph_dict)
print(check_if_connected(new_result_1))

# QUESTION 6: Increase N in line 14. Does the runtime for DFS scale as expected? Provide a plot to back your conclusion.
# Average search time over 1000 runs with N = 100.
print(f"The average time taken for DFS search over 1000 runs for the graph size 100 is {round(compute_search_time(1000, n=100), 6):.6f} seconds.")

# Plotting.
sizes = [i for i in range(10, 1000, 10)]
times = []

for size in sizes:
    times.append(compute_search_time(10, n=size))
    print(size)

plt.plot(sizes, times)
plt.xlabel('Size of the graph.')
plt.ylabel('Time')
plt.title('Depth First Search Runtime')

plt.grid(True)

plt.show()
