graph = {5: [3, 7], 3: [2, 4], 7: [8], 2: [], 4: [8], 8: []}

visited = set()


def dfs1(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for child in graph[node]:
            dfs1(visited, graph, child)


dfs1(visited, graph, 5)
