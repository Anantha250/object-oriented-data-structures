import sys
sys.setrecursionlimit(10**7)

class Dinic:
    class Edge:
        def __init__(self, to, cap, rev):
            self.to = to
            self.cap = cap
            self.rev = rev

    def __init__(self, n):
        self.n = n
        self.g = [[] for _ in range(n)]

    def add_edge(self, fr, to, cap):
        fwd = self.Edge(to, cap, len(self.g[to]))
        bwd = self.Edge(fr, 0, len(self.g[fr]))
        self.g[fr].append(fwd)
        self.g[to].append(bwd)

    def bfs(self, s, t, level):
        from collections import deque
        q = deque([s])
        level[s] = 0
        while q:
            v = q.popleft()
            for e in self.g[v]:
                if e.cap > 0 and level[e.to] < 0:
                    level[e.to] = level[v] + 1
                    q.append(e.to)
        return level[t] >= 0

    def dfs(self, v, t, f, level, it):
        if v == t:
            return f
        for i in range(it[v], len(self.g[v])):
            it[v] = i
            e = self.g[v][i]
            if e.cap > 0 and level[v] < level[e.to]:
                d = self.dfs(e.to, t, min(f, e.cap), level, it)
                if d > 0:
                    e.cap -= d
                    self.g[e.to][e.rev].cap += d
                    return d
        return 0

    def max_flow(self, s, t):
        flow = 0
        level = [-1] * self.n
        INF = 10**18
        while True:
            level = [-1] * self.n
            if not self.bfs(s, t, level):
                return flow
            it = [0] * self.n
            while True:
                f = self.dfs(s, t, INF, level, it)
                if f == 0:
                    break
                flow += f

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    dinic = Dinic(n)
    for _ in range(m):
        u, v, c = map(int, input().split())
        dinic.add_edge(u, v, c)
    s, t = map(int, input().split())
    print(dinic.max_flow(s, t))
