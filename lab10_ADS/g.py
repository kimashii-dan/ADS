from collections import defaultdict, deque
def detect_cycle_bfs(matrix, n):
    in_degree = {i: 0 for i in range(1, n + 1)}
    for node in matrix:
        for neighbor in matrix[node]:
            in_degree[neighbor] += 1

    queue = deque([node for node in in_degree if in_degree[node] == 0])
    processed_count = 0

    while queue:
        current = queue.popleft()
        processed_count += 1
        for neighbor in matrix[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)


    return processed_count != n


n, m = map(int, input().split())
D = defaultdict(list)
for _ in range(m):
    v, u = map(int, input().split())
    D[v].append(u)

print("Cycle detected:", detect_cycle_bfs(D, n))
