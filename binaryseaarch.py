


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder(node, result):
    if node is None:
        return
    inorder(node.left, result)
    result.append(node.data)
    inorder(node.right, result)


root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)
root.left.right = Node(40)
root.right.right = Node(80)

result = []
inorder(root, result)
print("Inorder traversal:", result)
