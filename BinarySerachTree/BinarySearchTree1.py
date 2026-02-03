class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

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

    def printTree(self, node, level=0):
        if node:
            self.printTree(node.right, level + 1)
            print('     ' * level + str(node))
            self.printTree(node.left, level + 1)


T = BST()
for i in map(int, input('Enter Input : ').split()):
    root = T.insert(i)

T.printTree(root)
