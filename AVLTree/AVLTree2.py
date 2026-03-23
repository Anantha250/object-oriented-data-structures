class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.height = 0

    def setHeight(self):
        self.height = 1 + max(self.getHeight(self.left), self.getHeight(self.right))

    def getHeight(self, node):
        return -1 if node is None else node.height

    def balanceValue(self):
        return self.getHeight(self.right) - self.getHeight(self.left)


class AVLTree:
    def __init__(self):
        self.root = None

    def add(self, data):
        self.root = self._add(self.root, int(data))

    def _add(self, root, data):
        if root is None:
            return Node(data)

        if data < root.data:
            root.left = self._add(root.left, data)
        else:
            root.right = self._add(root.right, data)

        root.setHeight()
        balance = root.balanceValue()

        if balance > 1:
            if data > root.right.data:
                return self.rotateLeft(root)
            else:
                root.right = self.rotateRight(root.right)
                return self.rotateLeft(root)

        if balance < -1:
            if data < root.left.data:
                return self.rotateRight(root)
            else:
                root.left = self.rotateLeft(root.left)
                return self.rotateRight(root)

        return root

    def rotateLeft(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        x.setHeight()
        y.setHeight()
        return y

    def rotateRight(self, x):
        y = x.left
        x.left = y.right
        y.right = x
        x.setHeight()
        y.setHeight()
        return y

    def printTree(self):
        self._printTree(self.root)

    def _printTree(self, node, level=0):
        if node:
            self._printTree(node.right, level + 1)
            print("     " * level + str(node.data))
            self._printTree(node.left, level + 1)


myTree = AVLTree()
data = input("Enter Input : ").split()

for e in data:
    print("insert :", e)
    myTree.add(e)
    myTree.printTree()
    print("===============")
