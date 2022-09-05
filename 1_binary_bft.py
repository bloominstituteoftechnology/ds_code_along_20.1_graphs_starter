from collections import deque

class node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def traverse(root: node):
    queue = deque()
    values = []

    # your BFT code here
    # Enqueue: queue.append(value)
    # Dequeue: queue.popleft(value)

    return values

# Implement a breadth-first traversal (BFT) for a binary tree. 
# Inputs: 
#   root: node (root of the binary tree)

# Output: list of values in the order of a breadth-first traversal 


# Test cases:
head = node(6)
head.left = node(3)
head.right = node(9)

print(traverse(head)) # 6, 3, 9