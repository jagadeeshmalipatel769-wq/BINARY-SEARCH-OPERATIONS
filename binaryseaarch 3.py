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


def find_min(node):
    while node.left is not None:
        node = node.left
    return node


def delete_node(node, value):
    if node is None:
        return None

    if value < node.data:
        node.left = delete_node(node.left, value)
    elif value > node.data:
        node.right = delete_node(node.right, value)
    else:
        if node.left is None:
            return node.right
        if node.right is None:
            return node.left

        successor = find_min(node.right)
        node.data = successor.data
        node.right = delete_node(node.right, successor.data)

    return node


def inorder(node, result):
    if node is None:
        return
    inorder(node.left, result)
    result.append(node.data)
    inorder(node.right, result)


root = None
for value in [50, 30, 70, 20, 40, 60, 80]:
    root = insert(root, value)

root = delete_node(root, 30)

result = []
inorder(root, result)
print("Inorder after deleting 30:", result)