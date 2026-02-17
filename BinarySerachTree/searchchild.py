class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert(self.root, data)
        return self.root

    def _insert(self, node, data):
        if node is None:
            return Node(data)
        if data < node.data:
            node.left = self._insert(node.left, data)
        else:
            node.right = self._insert(node.right, data)
        return node

    def search_val(self, val):
        return self._search(self.root, val)

    def _search(self, node, val):
        if node is None or node.data == val:
            return node
        if val < node.data:
            return self._search(node.left, val)
        return self._search(node.right, val)

    def search_child(self, node):
        if node is None:
            return []
        return (
            [node.data]
            + self.search_child(node.left)
            + self.search_child(node.right)
        )

    def printTree(self, node, level=0):
        if node:
            self.printTree(node.right, level + 1)
            print("     " * level + str(node))
            self.printTree(node.left, level + 1)


T = BST()

raw = input("Enter the BST values and search value: ").split(", ")
bst_values = list(map(int, raw[0].split()))
val = int(raw[1])

print(f"Input: root = {bst_values}, val = {val}")

for v in bst_values:
    T.insert(v)

found = T.search_val(val)
print("Output:", T.search_child(found))
