class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
        self.size = 1
        self.sum = key
        self.freq = 1


def height(n):
    return n.height if n else 0


def size(n):
    return n.size if n else 0


def subtree_sum(n):
    return n.sum if n else 0


def update(n):
    if not n:
        return
    n.height = 1 + max(height(n.left), height(n.right))
    n.size = size(n.left) + size(n.right) + n.freq
    n.sum = subtree_sum(n.left) + subtree_sum(n.right) + n.key * n.freq


def bf(n):
    return height(n.left) - height(n.right)


def rotate_right(y):
    x = y.left
    t = x.right
    x.right = y
    y.left = t
    update(y)
    update(x)
    return x


def rotate_left(x):
    y = x.right
    t = y.left
    y.left = x
    x.right = t
    update(x)
    update(y)
    return y


def balance(n):
    update(n)
    b = bf(n)
    if b > 1:
        if bf(n.left) < 0:
            n.left = rotate_left(n.left)
        return rotate_right(n)
    if b < -1:
        if bf(n.right) > 0:
            n.right = rotate_right(n.right)
        return rotate_left(n)
    return n


def insert(n, k):
    if not n:
        return Node(k)
    if k == n.key:
        n.freq += 1
    elif k < n.key:
        n.left = insert(n.left, k)
    else:
        n.right = insert(n.right, k)
    return balance(n)


def get_min(n):
    while n.left:
        n = n.left
    return n


def delete(n, k):
    if not n:
        return None
    if k < n.key:
        n.left = delete(n.left, k)
    elif k > n.key:
        n.right = delete(n.right, k)
    else:
        if n.freq > 1:
            n.freq -= 1
        else:
            if not n.left:
                return n.right
            if not n.right:
                return n.left
            t = get_min(n.right)
            n.key, n.freq = t.key, t.freq
            t.freq = 1
            n.right = delete(n.right, t.key)
    return balance(n) if n else None


def kth(n, k):
    if not n:
        return None
    if size(n.left) >= k:
        return kth(n.left, k)
    if size(n.left) + n.freq >= k:
        return n.key
    return kth(n.right, k - size(n.left) - n.freq)


def rank(n, k):
    if not n:
        return 0
    if k <= n.key:
        return rank(n.left, k)
    return size(n.left) + n.freq + rank(n.right, k)


def range_count(n, l, r):
    if not n:
        return 0
    if n.key < l:
        return range_count(n.right, l, r)
    if n.key > r:
        return range_count(n.left, l, r)
    return (
        range_count(n.left, l, r)
        + n.freq
        + range_count(n.right, l, r)
    )


def range_sum(n, l, r):
    if not n:
        return 0
    if n.key < l:
        return range_sum(n.right, l, r)
    if n.key > r:
        return range_sum(n.left, l, r)
    return (
        range_sum(n.left, l, r)
        + n.key * n.freq
        + range_sum(n.right, l, r)
    )