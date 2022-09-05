from collections import deque

def traverse(graph, root):
    pass

# Implement a breadth-first traversal (BFT) for a graph. 
# Inputs: 
#   graph: dict (adjacency list representation)
#   root: int (starting point for the traverse)

# Output: list of values in the order of a breadth-first traversal 

# Representing a graph as a Python dictionary provides a nice simplified version of an adjacency list implementation. The keys of the dictionary are vertices, and the key-value pairs in the dictionary map each vertex to a list of integers representing its neighbors.

# Test cases
# We'll be using this simple undirected graph to test our BFT:
# 5 -- 3
# | \
# |  2
# | / \
# 1    4
graph = {1: [2, 5], 2: [1, 4, 5], 3: [5], 4: [2], 5: [1, 2, 3]}
print(traverse(graph, 1)) # [1, 2, 5, 4, 3]
print(traverse(graph, 4)) # [4, 2, 1, 5, 3]
print(traverse(graph, 5)) # [5, 1, 2, 3, 4]