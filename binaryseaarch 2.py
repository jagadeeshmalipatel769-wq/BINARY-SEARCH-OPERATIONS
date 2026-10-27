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


def inorder(node, result):
    if node is None:
        return
    inorder(node.left, result)
    result.append(node.data)
    inorder(node.right, result)


root = None
for value in [50, 30, 70, 20, 40, 35]:
    root = insert(root, value)

result = []
inorder(root, result)
print("Inorder after insertion:", result)