n, m = map(int, input().split())
rows = [list(map(int, input().split())) for _ in range(n)]

sorted_rows = sorted(rows, key=lambda row: (-sum(row), row))

for row in sorted_rows:
    print(" ".join(map(str, row)) + " ")
