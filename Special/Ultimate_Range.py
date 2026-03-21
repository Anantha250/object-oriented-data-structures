import sys
input = sys.stdin.readline

class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.size = 1
        while self.size < n:
            self.size <<= 1
        self.sum = [0] * (2 * self.size)
        self.lazy_add = [0] * (2 * self.size)
        self.lazy_set = [0] * (2 * self.size)
        self.has_set = [False] * (2 * self.size)

    def apply_set(self, x, lx, rx, v):
        self.sum[x] = (rx - lx) * v
        self.lazy_set[x] = v
        self.has_set[x] = True
        self.lazy_add[x] = 0

    def apply_add(self, x, lx, rx, v):
        if self.has_set[x]:
            self.lazy_set[x] += v
        else:
            self.lazy_add[x] += v
        self.sum[x] += (rx - lx) * v

    def push(self, x, lx, rx):
        if rx - lx == 1:
            return
        mid = (lx + rx) // 2
        if self.has_set[x]:
            self.apply_set(2*x+1, lx, mid, self.lazy_set[x])
            self.apply_set(2*x+2, mid, rx, self.lazy_set[x])
            self.has_set[x] = False
        if self.lazy_add[x] != 0:
            self.apply_add(2*x+1, lx, mid, self.lazy_add[x])
            self.apply_add(2*x+2, mid, rx, self.lazy_add[x])
            self.lazy_add[x] = 0

    def range_add(self, l, r, v, x, lx, rx):
        if lx >= r or rx <= l:
            return
        if lx >= l and rx <= r:
            self.apply_add(x, lx, rx, v)
            return
        self.push(x, lx, rx)
        mid = (lx + rx) // 2
        self.range_add(l, r, v, 2*x+1, lx, mid)
        self.range_add(l, r, v, 2*x+2, mid, rx)
        self.sum[x] = self.sum[2*x+1] + self.sum[2*x+2]

    def range_set(self, l, r, v, x, lx, rx):
        if lx >= r or rx <= l:
            return
        if lx >= l and rx <= r:
            self.apply_set(x, lx, rx, v)
            return
        self.push(x, lx, rx)
        mid = (lx + rx) // 2
        self.range_set(l, r, v, 2*x+1, lx, mid)
        self.range_set(l, r, v, 2*x+2, mid, rx)
        self.sum[x] = self.sum[2*x+1] + self.sum[2*x+2]

    def range_sum(self, l, r, x, lx, rx):
        if lx >= r or rx <= l:
            return 0
        if lx >= l and rx <= r:
            return self.sum[x]
        self.push(x, lx, rx)
        mid = (lx + rx) // 2
        s1 = self.range_sum(l, r, 2*x+1, lx, mid)
        s2 = self.range_sum(l, r, 2*x+2, mid, rx)
        return s1 + s2

n, q = map(int, input().split())
st = SegmentTree(n)

for _ in range(q):
    t, *args = map(int, input().split())
    if t == 1:
        l, r, x = args
        st.range_add(l-1, r, x, 0, 0, st.size)
    elif t == 2:
        l, r, x = args
        st.range_set(l-1, r, x, 0, 0, st.size)
    else:
        l, r = args
        print(st.range_sum(l-1, r, 0, 0, st.size))