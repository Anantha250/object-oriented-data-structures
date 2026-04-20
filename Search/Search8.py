import heapq

def a_star(graph, start, goal, h):
    open_set = []
    heapq.heappush(open_set, (0, start))
    g = {start: 0}
    parent = {start: None}
    
    while open_set:
        _, node = heapq.heappop(open_set)
        
        if node == goal:
            path = []
            while node:
                path.append(node)
                node = parent[node]
            return path[::-1]
        
        for neighbor, cost in graph[node]:
            new_g = g[node] + cost
            if neighbor not in g or new_g < g[neighbor]:
                g[neighbor] = new_g
                f = new_g + h(neighbor)
                heapq.heappush(open_set, (f, neighbor))
                parent[neighbor] = node
    return None