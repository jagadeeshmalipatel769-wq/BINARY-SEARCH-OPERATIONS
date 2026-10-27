class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(node, value):
    if node is None:
        return Node(value)
    if value < node.data:
        node.left = insert(node.left, value)
    elif value > node.data:
        node.right = insert(node.right, value)
    return node


def height(node):
    if node is None:
        return -1
    return 1 + max(height(node.left), height(node.right))


balanced = None
for value in [40, 20, 60, 10, 30, 50, 70]:
    balanced = insert(balanced, value)

degenerate = None
for value in [10, 20, 30, 40, 50, 60, 70]:
    degenerate = insert(degenerate, value)

print("Balanced tree height:", height(balanced))
print("Degenerate tree height:", height(degenerate))