class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def is_valid_bst(node, min_val=float('-inf'), max_val=float('inf')):
    if node is None:
        return True

    if node.data <= min_val or node.data >= max_val:
        return False

    return (is_valid_bst(node.left, min_val, node.data) and
            is_valid_bst(node.right, node.data, max_val))


invalid_tree = Node(50)
invalid_tree.left = Node(30)
invalid_tree.left.right = Node(60)

valid_tree = Node(50)
valid_tree.left = Node(30)
valid_tree.right = Node(70)

print("Invalid tree check:", "valid" if is_valid_bst(invalid_tree) else "invalid")
print("Valid tree check:", "valid" if is_valid_bst(valid_tree) else "invalid")