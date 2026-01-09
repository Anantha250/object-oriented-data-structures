class Graph:
    def __init__(self, n=1000):
        self.n = n
        self.edge = [[] for _ in range(n)]
        self.color = [0] * n

    def add(self, u, v):
        self.edge[u].append(v)

    def dfs(self, u):
        if self.color[u] == 1:
            return True
        if self.color[u] == 2:
            return False

        self.color[u] = 1
        for v in self.edge[u]:
            if self.dfs(v):
                return True
        self.color[u] = 2
        return False

    def check(self):
        for u in range(self.n):
            if self.color[u] == 0 and self.dfs(u):
                return True
        return False


inp = [[int(k) for k in e.split()] for e in input("Enter : ").split(',')]
g = Graph()

for u, v in inp:
    g.add(u, v)

print("Graph has a cycle" if g.check() else "Graph has no cycle")
