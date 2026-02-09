from dataclasses import dataclass
from typing import Optional, List


@dataclass
class Node:
    data: str
    left: Optional["Node"] = None
    right: Optional["Node"] = None

    def __str__(self) -> str:
        return str(self.data)


class ExpressionTree:
    OPERATORS = {"+", "-", "*", "/", "%", "^"}

    def __init__(self) -> None:
        self.root: Optional[Node] = None

    def is_number(self, token: str) -> bool:
        if not token:
            return False
        try:
            float(token)
            return True
        except ValueError:
            return False

    def is_operand(self, token: str) -> bool:
        return self.is_number(token) or token.isidentifier()

    def build_tree(self, postfix: List[str]) -> Node:
        if not postfix:
            raise ValueError("Postfix expression is empty")

        stack: List[Node] = []

        for token in postfix:
            if self.is_operand(token):
                stack.append(Node(token))
                continue

            if token in self.OPERATORS:
                if len(stack) < 2:
                    raise ValueError(f"Not enough operands for operator '{token}'")
                right = stack.pop()
                left = stack.pop()
                stack.append(Node(token, left, right))
                continue

            raise ValueError(f"Unknown token: {token}")

        if len(stack) != 1:
            raise ValueError("Invalid postfix expression: leftover operands/operators")

        self.root = stack[0]
        return self.root

    def print_tree(self, node: Optional[Node] = None, level: int = 0) -> None:
        node = self.root if node is None else node
        if node is None:
            return

        if node.right is not None:
            self.print_tree(node.right, level + 1)

        print("     " * level + str(node))

        if node.left is not None:
            self.print_tree(node.left, level + 1)


def main() -> None:
    t = ExpressionTree()
    postfix = input("Enter Postfix Expression: ").split()

    try:
        t.build_tree(postfix)
        t.print_tree()
    except ValueError as e:
        print("Error:", e)