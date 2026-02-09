class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.height = 0
        self.setHeight()

    def __str__(self):
        return str(self.data)

    def getHeight(self, node):
        return -1 if node is None else node.height

    def setHeight(self):
        self.height = 1 + max(self.getHeight(self.left),
                              self.getHeight(self.right))
        return self.height

    def balanceValue(self):
        return self.getHeight(self.right) - self.getHeight(self.left)

    def _gen_display(self):
        if self is None:
            return [], 0, 0, 0

        lt, lf, lv, lb = Node._gen_display(self.left)
        rt, rf, rv, rb = Node._gen_display(self.right)
        data = str(self.data)

        if not lt and not rt:
            return [data], 0, len(data), 0

        add_left, add_right = int(bool(lt)), int(bool(rt))

        line = ((' ' * (lf + lv) + '/' + ' ' * lb) * add_left +
                ' ' * len(data) +
                (' ' * rf + '\\' + ' ' * (rv + rb)) * add_right)

        out = [' ' * (lf + lv + add_left) + '_' * lb + data +
               '_' * rf + ' ' * (rv + rb + add_right), line]

        if len(lt) > len(rt):
            rt.extend([' ' * (rf + rv + rb)] * (len(lt) - len(rt)))
        elif len(rt) > len(lt):
            lt.extend([' ' * (lf + lv + lb)] * (len(rt) - len(lt)))

        for l, r in zip(lt, rt):
            out.append(l + ' ' * (len(data) + add_left + add_right) + r)

        return out, (lf + lv + lb + add_left), len(data), (rf + rv + rb + add_right)


class AVLTree:
    def __init__(self):
        self.root = None

    def add(self, data):
        self.root = self._add(self.root, int(data))

    @staticmethod
    def _add(root, data):
        if not root:
            return Node(data)

        if data < root.data:
            root.left = AVLTree._add(root.left, data)
        else:
            root.right = AVLTree._add(root.right, data)

        root.setHeight()
        balance = root.balanceValue()

        if balance > 1:
            if data > root.right.data:
                return AVLTree.rotateLeft(root)
            root.right = AVLTree.rotateRight(root.right)
            return AVLTree.rotateLeft(root)

        if balance < -1:
            if data < root.left.data:
                return AVLTree.rotateRight(root)
            root.left = AVLTree.rotateLeft(root.left)
            return AVLTree.rotateRight(root)

        return root

    @staticmethod
    def rotateLeft(x):
        y = x.right
        if not y:
            return x

        x.right = y.left
        y.left = x
        x.setHeight()
        y.setHeight()
        return y

    @staticmethod
    def rotateRight(x):
        y = x.left
        if not y:
            return x

        x.left = y.right
        y.right = x
        x.setHeight()
        y.setHeight()
        return y

    def printTree(self):
        self._printTree(self.root)

    @staticmethod
    def _printTree(node, level=0):
        if node:
            AVLTree._printTree(node.right, level + 1)
            print('     ' * level + str(node.data))
            AVLTree._printTree(node.left, level + 1)


class Tree:
    def __init__(self):
        self.root = None

    def add_left(self, data):
        self.root = self._add_left(self.root, int(data))

    @staticmethod
    def _add_left(root, data):
        if not root:
            return Node(data)
        root.left = Tree._add_left(root.left, data)
        return root

    def add_right(self, data):
        self.root = self._add_right(self.root, int(data))

    @staticmethod
    def _add_right(root, data):
        if not root:
            return Node(data)
        root.right = Tree._add_right(root.right, data)
        return root

    def dfs(self):
        if not self.root:
            return []

        stack = [self.root]
        result = []

        while stack:
            node = stack.pop()
            result.append(node.data)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return result

    def find_node(self, data):
        cur = self.root
        parent = None

        while cur:
            if cur.data == data:
                return cur, parent

            parent = cur
            if data > cur.data:
                cur = cur.right
            else:
                cur = cur.left

        raise ValueError(f"No {data} in this tree")

    def merge_tree(self, parent, data, subtree):
        if data == self.root.data:
            self.root = subtree.root
        elif parent.left and parent.left.data == data:
            parent.left = subtree.root
        elif parent.right and parent.right.data == data:
            parent.right = subtree.root


def top_view(tree):
    img = tree.root._gen_display()
    print(*img[0], sep='\n')
    print("-" * sum(img[1:]))

def top_view_normal(tree):
    img = tree.root._gen_display()
    print(*img[0], sep='\n')


data = input("Enter input: ").split(',')
rotate_node = int(data[0])
rotate_direct = data[1][0]
values = data[2].split()

myTree = AVLTree()

print("Before")
for v in values:
    myTree.add(v)

top_view(myTree)

tree = Tree()
tree.root = myTree.root

cut_tree = Tree()
cut_tree.root, parent = tree.find_node(rotate_node)
sorted_nodes = sorted(cut_tree.dfs())

new_tree = Tree()

if rotate_direct == "l":
    for v in reversed(sorted_nodes):
        new_tree.add_left(v)
else:
    for v in sorted_nodes:
        new_tree.add_right(v)

tree.merge_tree(parent, rotate_node, new_tree)

print("After")
top_view_normal(tree)
