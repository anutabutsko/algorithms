# Shortest Path with Bellman-Ford Algorithm

This Python script demonstrates the Bellman-Ford algorithm to find the shortest path from a source vertex to all other vertices in a graph. It also includes path tracking from the source to each destination vertex.

## Usage

1. Import the `initialize_graph` function from the `graphs.py` file.
2. Create an instance of the `Graph` class.
3. Initialize the graph with vertices and edges using the `initialize_graph` function.
4. Run the Bellman-Ford algorithm with a specified source vertex to find the shortest paths.
5. The algorithm will print the shortest distances and paths from the source vertex to all other vertices.

# Output Example

```python
Shortest distance from node 0 to node 20 is 9.
Path: 0 -> 1 -> 14 -> 16 -> 20
