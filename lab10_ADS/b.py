from collections import deque
def shortest_distance_bfs(matrix, start, end):
    n = len(matrix)
    visited = [False] * n
    distance = [-1] * n
    queue = deque([start])

    visited[start] = True
    distance[start] = 0
    
    while queue:
        current = queue.popleft()
        if current == end:
            return distance[current]

        for neighbor in range(n):
            if matrix[current][neighbor] == 1 and not visited[neighbor]:
                visited[neighbor] = True
                distance[neighbor] = distance[current] + 1
                queue.append(neighbor)
    

    return -1

n = int(input())
M = []
for i in range(n):
    row = list(map(int, input().split()[:n]))
    M.append(row)

a, b = map(int, input().split())
print(shortest_distance_bfs(M, a - 1, b - 1))