import sys


def count_node_memory(node_count):
    bytes_per_node = sys.getsizeof(0) + 2 * 8
    return node_count * bytes_per_node


def count_array_memory(element_count):
    return element_count * sys.getsizeof(0)


n = 1000

print(f"Approximate BST memory for {n} nodes:", count_node_memory(n), "bytes")
print(f"Approximate array memory for {n} elements:", count_array_memory(n), "bytes")