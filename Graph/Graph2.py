from collections import deque

raw = input("Enter : ").strip()
pairs = [p.strip().split() for p in raw.split(",") if p.strip()]

n = 0
edges = []
for p in pairs:
    if len(p) < 2:
        continue
    u = ord(p[0]) - ord("A")
    v = ord(p[1]) - ord("A")
    edges.append((u, v))
    n = max(n, u + 1, v + 1)

adj = [[] for _ in range(n)]
for u, v in edges:
    adj[u].append(v)
    adj[v].append(u)

for i in range(n):
    adj[i].sort()

dfs_order = []
dfs_visited = [False] * n

def dfs(s):
    stack = [s]
    while stack:
        u = stack.pop()
        if dfs_visited[u]:
            continue
        dfs_visited[u] = True
        dfs_order.append(u)
        for v in reversed(adj[u]):
            if not dfs_visited[v]:
                stack.append(v)

bfs_order = []
bfs_visited = [False] * n

def bfs(s):
    q = deque([s])
    while q:
        u = q.popleft()
        if bfs_visited[u]:
            continue
        bfs_visited[u] = True
        bfs_order.append(u)
        for v in adj[u]:
            if not bfs_visited[v]:
                q.append(v)

for i in range(n):
    if not dfs_visited[i]:
        dfs(i)
    if not bfs_visited[i]:
        bfs(i)

print("Depth First Traversals :", " ".join(chr(x + ord("A")) for x in dfs_order))
print("Bredth First Traversals :", " ".join(chr(x + ord("A")) for x in bfs_order))
