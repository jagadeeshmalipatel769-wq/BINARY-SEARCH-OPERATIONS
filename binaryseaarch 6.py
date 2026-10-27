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


def find_lca(node, target1, target2):
    while node is not None:
        if target1 < node.data and target2 < node.data:
            node = node.left
        elif target1 > node.data and target2 > node.data:
            node = node.right
        else:
            return node
    return None


root = None
for value in [50, 30, 70, 20, 40]:
    root = insert(root, value)

lca1 = find_lca(root, 20, 40)
print("LCA of 20 and 40:", lca1.data)

lca2 = find_lca(root, 20, 70)
print("LCA of 20 and 70:", lca2.data)