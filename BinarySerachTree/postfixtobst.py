class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


class ExpressionTree:
    def __init__(self):
        self.root = None
        self.operators = ['+', '-', '*', '/', '%', '^']

    def is_operand(self, token):
        try:
            float(token)
            return True
        except:
            pass

        return token.isidentifier()

    def buildTree(self, postfix):
        if len(postfix) == 0:
            raise ValueError("Postfix expression is empty")

        stack = []

        for token in postfix:
            if self.is_operand(token):
                stack.append(Node(token))
            elif token in self.operators:
                if len(stack) < 2:
                    raise ValueError("Invalid postfix expression")
                right = stack.pop()
                left = stack.pop()
                stack.append(Node(token, left, right))
            else:
                raise ValueError("Unknown token: " + token)

        if len(stack) != 1:
            raise ValueError("Invalid postfix expression")

        self.root = stack[0]
        return self.root

    def printTree(self, node=None, level=0):
        if node is None:
            node = self.root
        if node is None:
            return

        if node.right:
            self.printTree(node.right, level + 1)
        print('     ' * level + str(node))
        if node.left:
            self.printTree(node.left, level + 1)


T = ExpressionTree()
postfix = input('Enter Postfix Expression: ').split()

try:
    root = T.buildTree(postfix)
    T.printTree(root)
except ValueError as e:
    print("Error:", e)
