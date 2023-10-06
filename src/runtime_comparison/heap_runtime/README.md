# Max Heap Algorithm Runtime Analysis

## Introduction
The script focuses on the runtime analysis of the Max Heap algorithm. Specifically, it provides the functionality of heapifying an array (transforming it into a max heap) and then evaluates its performance concerning various input sizes. The runtime analysis is visualized using a plot that displays the relationship between the input size and the average execution time of the `build_max_heap` function.

## Dependencies
- `timeit`: Standard library module used for measuring the execution time of small bits of Python code.
- `random`: Standard library module used for generating random numbers.
- `statistics`: Standard library module used for mathematical statistics of numeric data.
- `matplotlib`: Used for plotting graphs.

## Functionalities

### 1. `max_heapify(array, i)`: 
- **Objective**: Ensure the subtree rooted at `i` adheres to the heap property (parent node >= child nodes).
- **Argument**: An array and an index `i`.

### 2. `build_max_heap(array)`:
- **Objective**: Convert `array` into a max heap by iteratively applying `max_heapify`.
- **Argument**: An array.

### 3. `generate_random_list(length)`:
- **Objective**: Generate a list of random integers.
- **Argument**: The desired length of the list.
- **Returns**: A list of random integers between 0 and 1000.

## Script Workflow
1. Define different sizes of lists to be tested (`len_lsts`).
2. For each size, generate 1000 random lists, build max heaps, and measure the runtime.
3. Compute the average runtime for each list size.
4. Plot the average runtimes against list sizes.
5. Save and display the generated plot, showing the trend in the algorithm's runtime with varying input sizes.

## Usage
1. Execute the script to visualize the average runtime growth of the Max Heap Algorithm as the list size increases.
2. Analyze the resulting graph for insights into how the max heap algorithm's efficiency varies with the input size.

## Observation
The plot depicts the growth of the algorithm's runtime concerning input size. Even though the complexity of building a max heap is often considered to be \(\Theta(n log(n))\), examining the graph allows you to empirically observe its behavior under different conditions and with varied data. The accompanying comments within the script indicate a potential discrepancy between expected and observed results, opening a door for further investigation and study in algorithmic behavior and computational complexity.

## Conclusion
This script serves as an empirical analysis tool to explore and visualize the runtime efficiency of the Max Heap Algorithm. Such a tool assists not only in validating theoretical complexities but also provides insights into the practical aspects and applications of the algorithm in real-world scenarios, notably in sorting, priority queues, and data stream management.