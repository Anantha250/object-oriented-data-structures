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
        if self.root is None:
            self.root = Node(data)
            return self.root

        cur = self.root
        while True:
            if data < cur.data:
                if cur.left is None:
                    cur.left = Node(data)
                    break
                cur = cur.left
            else:
                if cur.right is None:
                    cur.right = Node(data)
                    break
                cur = cur.right
        return self.root

    def search_val(self, val):
        cur = self.root
        while cur:
            if val == cur.data:
                return cur
            cur = cur.left if val < cur.data else cur.right
        return None

    def search_child(self, node):
        if node is None:
            return []
        return [node.data] + self.search_child(node.left) + self.search_child(node.right)

    def printTree(self, node, level=0):
        if node:
            self.printTree(node.right, level + 1)
            print("     " * level, node)
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
