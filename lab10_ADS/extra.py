from collections import deque

def num_islands(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def bfs(row, col):
        queue = deque([(row, col)])
        visited[row][col] = True

        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and grid[nx][ny] == '1':
                    visited[nx][ny] = True
                    queue.append((nx, ny))

    islands = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1' and not visited[i][j]:
                bfs(i, j)
                islands += 1

    return islands


n, m = map(int, input().split())
grid = [input().strip() for _ in range(n)]


print(num_islands(grid))
