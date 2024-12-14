def nugman_and_graph(n, a, x):
    INF = float('inf')
    x.reverse()
    dist = [[INF] * n for _ in range(n)]


    for i in range(n):
        for j in range(n):
            if i == j:
                dist[i][j] = 0
            else:
                dist[i][j] = a[i][j]

    result = []
    active = set()

    for k in x:
        k -= 1
        active.add(k)

        for i in active:
            for j in active:
                for m in active:
                    dist[j][m] = min(dist[j][m], dist[j][i] + dist[i][m])

        longest_shortest = 0
        for i in active:
            for j in active:
                if i != j:
                    longest_shortest = max(longest_shortest, dist[i][j])
        
        result.append(longest_shortest if longest_shortest < INF else 0)

    return result[::-1]



# n = 4
# a = [
#     [0, 3, 1, 1],
#     [6, 0, 400, 1],
#     [2, 4, 0, 1],
#     [1, 1, 1, 0]
# ]
# x = [4, 1, 2, 3]

n = int(input())
M = []
for i in range(n):
    row = list(map(int, input().split()[:n]))
    M.append(row)

x = list(map(int, input().split()[:n]))

output = nugman_and_graph(n, M, x)
print(output)