graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

target = input("Enter node to search: ")

stack = ['A']
visited = []

while stack:
    node = stack.pop()
    if node not in visited:
        visited.append(node)
        if node == target:
            print("Found node", node)
            break
        stack.extend(graph[node])
else:
    print("Not found")