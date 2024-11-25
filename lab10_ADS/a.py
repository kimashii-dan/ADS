from collections import deque

def mario_war(m, n, grid):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque()
    mushrooms = 0
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                queue.append((i, j))
            elif grid[i][j] == 1:
                mushrooms += 1


    if mushrooms == 0:
        return 0

    minutes = 0
    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                    grid[nx][ny] = 2
                    queue.append((nx, ny))
                    mushrooms -= 1

        if queue:
            minutes += 1

    return minutes if mushrooms == 0 else -1




n, m = map(int, input().split())
M = []
for i in range(n):
    row = list(map(int, input().split()[:m]))
    M.append(row)


print(mario_war(n, m, M))