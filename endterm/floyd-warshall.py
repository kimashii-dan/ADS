def floyd_warshall(graph):
    n = len(graph)
    dist = [row[:] for row in graph]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


graph = [
    [0, 3, float('inf'), 7],
    [8, 0, 2, float('inf')],
    [float('inf'), float('inf'), 0, 1],
    [2, float('inf'), float('inf'), 0]
]


shortest_paths = floyd_warshall(graph)


for row in shortest_paths:
    print(row)