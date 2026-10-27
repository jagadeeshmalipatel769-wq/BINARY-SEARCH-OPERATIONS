class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = parent


def find_min(node):
    while node.left is not None:
        node = node.left
    return node


def find_successor(node):
    if node.right is not None:
        return find_min(node.right)
    ancestor = node.parent
    while ancestor is not None and node == ancestor.right:
        node = ancestor
        ancestor = ancestor.parent
    return ancestor


root = Node(50)
root.left = Node(30, root)
root.right = Node(70, root)
root.left.left = Node(20, root.left)
root.left.right = Node(40, root.left)

successor_of_30 = find_successor(root.left)
print("Successor of 30:", successor_of_30.data)

successor_of_40 = find_successor(root.left.right)
print("Successor of 40:", successor_of_40.data)