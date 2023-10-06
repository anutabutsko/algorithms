# Binary Search Tree (BST) Implementation

## Overview

This repository contains a Python implementation of the Binary Search Tree (BST) data structure. The implementation provides core BST operations including insertion, traversal, and searching.

## Implementation Details

- The `Node` class represents each node in the BST. Each node contains:
  - `value`: The data value of the node.
  - `left`: Reference to the left child of the node.
  - `right`: Reference to the right child of the node.

### Methods

1. **`insert(value)`**: Inserts a new value into the BST. The method places the new value in the appropriate position based on BST properties.

2. **`traverse()`**: Performs an in-order traversal of the BST and prints out the values of the nodes in ascending order.

3. **`search(value)`**: Searches the BST for a particular value and returns `True` if the value is found, otherwise `False`.

## Example Usage

```python
BST = Node(6)
BST.insert(13)
BST.insert(15)
BST.insert(3)
BST.insert(1)
BST.insert(8)
BST.insert(10)
BST.insert(7)
BST.insert(21)
BST.insert(14)

BST.traverse() # Outputs: 1 3 6 7 8 10 13 14 15 21

print(BST.search(14)) # Outputs: True
print(BST.search(56)) # Outputs: False
