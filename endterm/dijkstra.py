import heapq

def dijkstra(n, graph, src):
    dist = [float('inf')] * n
    dist[src] = 0
    pq = [(0, src)]

    while pq:
        current_dist, node = heapq.heappop(pq)
        if current_dist > dist[node]:
            continue
        for neighbor, weight in graph[node]:
            distance = current_dist + weight
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return dist


n = 5
graph = {
    0: [(1, 10), (2, 3)],
    1: [(3, 2)],
    2: [(1, 1), (3, 8)],
    3: [(4, 7)],
    4: []
}
src = 0

print(dijkstra(n, graph, src))
