from time import perf_counter

import numpy as np

from graph import generate_graph


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
    # Convert the graph to a dictionary representation.
    graph = convert(graph)
    # Initialize time to track the discovery and finish times.
    time = [0]

    # Initialize all vertices in the graph as unvisited, marking them with color "white".
    for vertex in graph:
        graph[vertex]["color"] = "white"
        graph[vertex]["previous"] = None

    # Iterate over each vertex in the graph.
    for vertex in graph:
        # If the vertex is unvisited, start the exploration process.
        if graph[vertex]["color"] == "white":
            explore(graph, vertex, time)

    return graph


# Function to explore the graph starting from a given vertex.
def explore(graph, vertex, time):
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
            explore(graph, connection, time)

    # Once exploration is complete, mark the vertex as finished.
    graph[vertex]["color"] = "black"

    # Increment the finish time for this vertex.
    time[0] += 1
    graph[vertex]["finish_time"] = time[0]


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
        # Start timer.
        start = perf_counter()

        # Generate graph without setting seed value to ensure a new graph is generated every time.
        if n:
            # Adjust number N.
            graph = generate_graph(n)
        else:
            graph = generate_graph()
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

    return f"The average time taken for DFS search over {runs} runs is {average_time:.6f} seconds."


# Find the greatest distance between any two connected points in the graph
def greatest_distance(graph):
    greatest = 0

    # Iterate over each vertex in the result.
    for vertex in graph:
        # Check if the finish time of the current vertex is greater than the current greatest distance.
        if graph[vertex]["finish_time"] > greatest:
            # If true, update the greatest distance to the finish time of this vertex.
            greatest = graph[vertex]["finish_time"]

    return f"The greatest distance between any two connected points in the graph is {greatest}."


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

# Perform Depth First Search on the graph and print the result.
result = DFS(graph)
print(result)

# Check if the underlying graph is connected.
print(check_if_connected(result))

# Average search time over 10000 runs.
print(compute_search_time(10000))

# QUESTION 3: What is the greatest distance between any two connected points in the graph?
print(greatest_distance(result))

# QUESTION 5: Change the random integer calls in lines 16, 20 and 24 to draw either 0 or 1. Does the graph remain connected?
new_graph_1 = generate_graph(start=0, end=1)
new_result_1 = DFS(new_graph_1)
print(check_if_connected(new_result_1))

# QUESTION 6: Increase N in line 14. Does the runtime for DFS scale as expected? Provide a plot to back your conclusion.
# Average search time over 10000 runs with N = 1000.
print(compute_search_time(10000, n=1000))


