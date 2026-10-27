class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def search(node, target):
    if node is None:
        return False
    if node.data == target:
        return True
    if target < node.data:
        return search(node.left, target)
    return search(node.right, target)


root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)
root.left.right = Node(40)

print("Searching for 40:", "found" if search(root, 40) else "not found")
print("Searching for 45:", "found" if search(root, 45) else "not found")