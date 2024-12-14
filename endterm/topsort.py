def dfs(node, graph, visited, result):
    if node in visited:
        return
    visited.add(node)
    for neighbor in graph[node]:
        dfs(neighbor, graph, visited, result)
    result.append(node)

def topological_sort(graph):
    visited = set()
    result = []
    for node in graph:
        if node not in visited:
            dfs(node, graph, visited, result)
    return result[::-1]

graph = {
    "A": ["C"],
    "B": ["C", "D"],
    "C": ["E"],
    "D": ["F"],
    "E": ["H", "F"],
    "F": ["G"],
    "G": [],
    "H": []
}

sorted_order = topological_sort(graph)
print("Topological Sort Order:", sorted_order)