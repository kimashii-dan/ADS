def dfs_from_matrix(matrix, start):
    visited = set()
    stack = [start]
    path = []
    while stack:
        node = stack.pop()
        path.append(node)
        for neighbor in range(len(matrix[node]) - 1, -1, -1):
            if matrix[node][neighbor] == 1 and neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)

    return path


n = int(input())
M = []
for i in range(n):
    row = list(map(int, input().split()[:n]))
    M.append(row)

print(M)

print(dfs_from_matrix(M, 0))