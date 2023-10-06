# Bubble Sort Algorithm Implementation and Analysis

## Overview

This repository provides an implementation and runtime analysis of the Bubble Sort algorithm. Bubble Sort is a simple comparison-based sorting technique where adjacent elements are swapped if they're in the wrong order. This operation continues until the list is fully sorted.

## Implementation Details

- The **`generate_random_list(length)`** function returns a random list of a given length containing values between 0 and 1000.

- The **`swap(input_lst, pos1, pos2)`** function swaps the positions of two elements in a list.

- The **`bubble_sort(lst)`** function sorts an input list using the Bubble Sort algorithm. The function's time complexity is generally represented as \( T(n) = O(n²) \), which is derived from the nested loop structure.

## Runtime Analysis

The main script includes a section for computing the average runtime of the Bubble Sort algorithm over 1000 iterations on random lists of varying sizes. This helps to empirically illustrate the algorithm's quadratic time complexity.

A plot is generated to visualize how the average runtime of the algorithm increases as the number of elements in the input list grows.

## Example Usage

```python
A = [1, 2, 3, 4, 5, 10, 9, 8, 7, 6]
print(bubble_sort(A))
```



