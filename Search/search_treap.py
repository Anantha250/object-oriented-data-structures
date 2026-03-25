import random

class Node:
    def __init__(self, key):
        self.key = key
        self.priority = random.random()
        self.count = 1
        self.size = 1
        self.left = None
        self.right = None

def size(node):
    return node.size if node else 0

def update(node):
    if node:
        node.size = size(node.left) + size(node.right) + node.count

def rotate_right(t):
    l = t.left
    t.left = l.right
    l.right = t
    update(t)
    update(l)
    return l

def rotate_left(t):
    r = t.right
    t.right = r.left
    r.left = t
    update(t)
    update(r)
    return r

def insert(t, key):
    if not t:
        return Node(key)
    
    if key == t.key:
        t.count += 1
    elif key < t.key:
        t.left = insert(t.left, key)
        if t.left.priority > t.priority:
            t = rotate_right(t)
    else:
        t.right = insert(t.right, key)
        if t.right.priority > t.priority:
            t = rotate_left(t)
    
    update(t)
    return t

def delete(t, key):
    if not t:
        return None
    
    if key == t.key:
        if t.count > 1:
            t.count -= 1
        else:
            if not t.left:
                return t.right
            elif not t.right:
                return t.left
            else:
                if t.left.priority > t.right.priority:
                    t = rotate_right(t)
                    t.right = delete(t.right, key)
                else:
                    t = rotate_left(t)
                    t.left = delete(t.left, key)
    elif key < t.key:
        t.left = delete(t.left, key)
    else:
        t.right = delete(t.right, key)
    
    update(t)
    return t

def kth(t, k):
    if not t:
        return None
    
    if k <= size(t.left):
        return kth(t.left, k)
    elif k > size(t.left) + t.count:
        return kth(t.right, k - size(t.left) - t.count)
    else:
        return t.key

def count_leq(t, x):
    if not t:
        return 0
    if t.key <= x:
        return size(t.left) + t.count + count_leq(t.right, x)
    else:
        return count_leq(t.left, x)

def count_range(t, l, r):
    return count_leq(t, r) - count_leq(t, l - 1)

def median(t):
    if not t:
        return None
    n = size(t)
    return kth(t, (n + 1) // 2)

# Merge Treap
def merge(a, b):
    if not a or not b:
        return a or b
    if a.priority > b.priority:
        a.right = merge(a.right, b)
        update(a)
        return a
    else:
        b.left = merge(a, b.left)
        update(b)
        return b