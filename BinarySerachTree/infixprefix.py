from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, List, Iterable

OPS = set("+-*/")


@dataclass
class Node:
    data: str
    left: Optional["Node"] = None
    right: Optional["Node"] = None

    def __str__(self) -> str:
        return str(self.data)


class Stack:
    def __init__(self) -> None:
        self._s: List[Node] = []

    def push(self, item: Node) -> None:
        self._s.append(item)

    def pop(self) -> Node:
        if not self._s:
            raise ValueError("Invalid postfix: stack underflow")
        return self._s.pop()

    def __len__(self) -> int:
        return len(self._s)


def tokenize_postfix(expr: str) -> List[str]:
    expr = expr.strip()
    if not expr:
        return []
    if " " in expr:
        return expr.split()
    return list(expr)


def build_expr_tree(postfix_tokens: List[str]) -> Node:
    st = Stack()
    for tok in postfix_tokens:
        if tok in OPS:
            r = st.pop()
            l = st.pop()
            st.push(Node(tok, l, r))
        else:
            st.push(Node(tok))

    if len(st) != 1:
        raise ValueError("Invalid postfix: leftover operands/operators")
    return st.pop()


def to_infix(node: Node) -> str:
    if node.data not in OPS:
        return node.data
    return f"({to_infix(node.left)}{node.data}{to_infix(node.right)})"


def to_prefix(node: Node) -> str:
    if node.data not in OPS:
        return node.data
    return f"{node.data}{to_prefix(node.left)}{to_prefix(node.right)}"


def print_tree(node: Optional[Node], level: int = 0) -> None:
    if node is None:
        return
    print_tree(node.right, level + 1)
    print("     " * level + str(node))
    print_tree(node.left, level + 1)


def main() -> None:
    inp = input("Enter Postfix : ")
    tokens = tokenize_postfix(inp)
    if not tokens:
        print("Tree :")
        print("(empty)")
        print("-" * 50)
        print("Infix :")
        print("Prefix :")
        return

    root = build_expr_tree(tokens)

    print("Tree :")
    print_tree(root)
    print("-" * 50)

    infix = to_infix(root)
    prefix = to_prefix(root)

    print("Infix :", infix)
    print("Prefix :", prefix)