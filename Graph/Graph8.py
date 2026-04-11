from collections import deque
import heapq


class DisjointSet:
	def __init__(self, n):
		self.parent = list(range(n + 1))
		self.rank = [0] * (n + 1)

	def find(self, x):
		while self.parent[x] != x:
			self.parent[x] = self.parent[self.parent[x]]
			x = self.parent[x]
		return x

	def union(self, a, b):
		ra = self.find(a)
		rb = self.find(b)
		if ra == rb:
			return False
		if self.rank[ra] < self.rank[rb]:
			ra, rb = rb, ra
		self.parent[rb] = ra
		if self.rank[ra] == self.rank[rb]:
			self.rank[ra] += 1
		return True


class Graph:
	def __init__(self, n, directed=False):
		self.n = n
		self.directed = directed
		self.adj = [[] for _ in range(n + 1)]
		self.edges = []

	def add_edge(self, u, v, w=1):
		self.adj[u].append((v, w))
		self.edges.append((u, v, w))
		if not self.directed:
			self.adj[v].append((u, w))

	def bfs_path(self, start, target):
		parent = [-1] * (self.n + 1)
		q = deque([start])
		parent[start] = start

		while q:
			u = q.popleft()
			if u == target:
				break
			for v, _ in self.adj[u]:
				if parent[v] == -1:
					parent[v] = u
					q.append(v)

		if parent[target] == -1:
			return None

		path = [target]
		cur = target
		while cur != start:
			cur = parent[cur]
			path.append(cur)
		path.reverse()
		return path

	def dijkstra(self, start, target):
		inf = 10**18
		dist = [inf] * (self.n + 1)
		parent = [-1] * (self.n + 1)
		dist[start] = 0
		parent[start] = start
		pq = [(0, start)]

		while pq:
			d, u = heapq.heappop(pq)
			if d != dist[u]:
				continue
			if u == target:
				break
			for v, w in self.adj[u]:
				nd = d + w
				if nd < dist[v]:
					dist[v] = nd
					parent[v] = u
					heapq.heappush(pq, (nd, v))

		if dist[target] == inf:
			return None, None

		path = [target]
		cur = target
		while cur != start:
			cur = parent[cur]
			path.append(cur)
		path.reverse()
		return dist[target], path

	def connected_components(self):
		visited = [False] * (self.n + 1)
		comps = []

		for s in range(1, self.n + 1):
			if visited[s]:
				continue
			comp = []
			q = deque([s])
			visited[s] = True
			while q:
				u = q.popleft()
				comp.append(u)
				for v, _ in self.adj[u]:
					if not visited[v]:
						visited[v] = True
						q.append(v)
			comps.append(sorted(comp))

		return comps

	def has_cycle_undirected(self):
		visited = [False] * (self.n + 1)

		def dfs(u, p):
			visited[u] = True
			for v, _ in self.adj[u]:
				if not visited[v]:
					if dfs(v, u):
						return True
				elif v != p:
					return True
			return False

		for i in range(1, self.n + 1):
			if not visited[i] and dfs(i, -1):
				return True
		return False

	def has_cycle_directed(self):
		color = [0] * (self.n + 1)

		def dfs(u):
			color[u] = 1
			for v, _ in self.adj[u]:
				if color[v] == 1:
					return True
				if color[v] == 0 and dfs(v):
					return True
			color[u] = 2
			return False

		for i in range(1, self.n + 1):
			if color[i] == 0 and dfs(i):
				return True
		return False

	def topological_sort(self):
		indeg = [0] * (self.n + 1)
		for u in range(1, self.n + 1):
			for v, _ in self.adj[u]:
				indeg[v] += 1

		q = deque([i for i in range(1, self.n + 1) if indeg[i] == 0])
		order = []
		while q:
			u = q.popleft()
			order.append(u)
			for v, _ in self.adj[u]:
				indeg[v] -= 1
				if indeg[v] == 0:
					q.append(v)

		if len(order) != self.n:
			return None
		return order

	def mst_kruskal(self):
		dsu = DisjointSet(self.n)
		total = 0
		used_edges = []

		for u, v, w in sorted(self.edges, key=lambda x: x[2]):
			if dsu.union(u, v):
				total += w
				used_edges.append((u, v, w))

		if len(used_edges) != self.n - 1:
			return None, None
		return total, used_edges


def solve():
	"""
	Ultimate Graph Data Structure Problem

	Input format:
	n m type
	u1 v1 w1
	...
	um vm wm
	q
	QUERY ...

	type: U (undirected) or D (directed)

	Supported queries:
	SHORTEST s t     -> weighted shortest path with Dijkstra
	BFS_PATH s t     -> unweighted shortest path with BFS
	COMPONENTS       -> list connected components (for undirected graphs)
	HAS_CYCLE        -> detect cycle
	TOPO             -> topological order (directed only)
	MST              -> minimum spanning tree total weight (undirected only)

	Example:
	5 6 U
	1 2 4
	1 3 2
	2 3 1
	2 4 5
	3 5 10
	4 5 3
	6
	SHORTEST 1 5
	BFS_PATH 1 5
	COMPONENTS
	HAS_CYCLE
	TOPO
	MST
	"""
	n, m, gtype = input().split()
	n = int(n)
	m = int(m)
	directed = gtype.upper() == "D"

	g = Graph(n, directed=directed)
	for _ in range(m):
		u, v, w = map(int, input().split())
		g.add_edge(u, v, w)

	q = int(input())
	for _ in range(q):
		parts = input().split()
		if not parts:
			continue

		cmd = parts[0].upper()

		if cmd == "SHORTEST":
			s, t = map(int, parts[1:3])
			dist, path = g.dijkstra(s, t)
			if path is None:
				print("NO PATH")
			else:
				print("DIST", dist, "PATH", "->".join(map(str, path)))

		elif cmd == "BFS_PATH":
			s, t = map(int, parts[1:3])
			path = g.bfs_path(s, t)
			if path is None:
				print("NO PATH")
			else:
				print("LEN", len(path) - 1, "PATH", "->".join(map(str, path)))

		elif cmd == "COMPONENTS":
			if directed:
				print("COMPONENTS query is for undirected graph only")
			else:
				comps = g.connected_components()
				print("COUNT", len(comps))
				for i, comp in enumerate(comps, 1):
					print(f"C{i}", *comp)

		elif cmd == "HAS_CYCLE":
			has_cycle = g.has_cycle_directed() if directed else g.has_cycle_undirected()
			print("YES" if has_cycle else "NO")

		elif cmd == "TOPO":
			if not directed:
				print("TOPO query is for directed graph only")
			else:
				order = g.topological_sort()
				if order is None:
					print("IMPOSSIBLE")
				else:
					print(*order)

		elif cmd == "MST":
			if directed:
				print("MST query is for undirected graph only")
			else:
				total, edges = g.mst_kruskal()
				if edges is None:
					print("NO MST")
				else:
					print("WEIGHT", total)
					for u, v, w in edges:
						print(u, v, w)

		else:
			print("UNKNOWN QUERY")


if __name__ == "__main__":
	solve()
