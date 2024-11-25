def count_islands(grid, n, m):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for i in range(n):
        for j in range(m):
            

n, m = map(int, input().split())
M = []
for i in range(n):
    row = list(map(int, input()[:m]))
    M.append(row)

print(M)

