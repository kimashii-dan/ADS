from collections import defaultdict
def bfs(matrix, start):
    visited = set()
    queue = [start]
    visited.add(start)
    result = []
    while queue:
        node = queue.pop(0)
        result.append(node)
        for nei_node in matrix[node]:
            if nei_node not in visited:
                visited.add(nei_node)
                queue.append(nei_node)
    return result



n, m = map(int, input().split())
D = defaultdict(list)
for i in range(m):
    v, u = map(int, input().split())
    D[v].append(u)

print(bfs(D, 1))