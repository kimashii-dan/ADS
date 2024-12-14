def bfs_from_matrix(matrix, start):
    visited = set()
    queue = [start]
    visited.add(start)
    path = []
    
    while queue:
        node = queue.pop(0)
        path.append(node)
        for neighbor in range(len(matrix[node])):
            if matrix[node][neighbor] == 1 and neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return path


n = int(input())
M = []
for i in range(n):
    row = list(map(int, input().split()[:n]))
    M.append(row)

print(M)

print(bfs_from_matrix(M, 0))