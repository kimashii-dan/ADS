import heapq

def djikstra(n, graph, src):
    dist = [float('inf')] * n
    dist[src] = 0
    pq = [(0, src)]

    while pq:
        current_dist, node =  heapq.heappop(pq)

        if current_dist > dist[node]:
            continue

        for neighbour, weight in graph[node]:
            distance = current_dist + weight
            if distance < dist[neighbour]:
                dist[neighbour] = distance
                heapq.heappush(pq, (distance, neighbour))

    return dist




def bfs(start, graph):
    queue = [start]
    visited = set()
    visited.add(start)
    path = []

    while queue:
        node = queue.pop(0)
        path.append(node)

        for neighbour in range(len(graph)):
            if graph[node][neighbour] == 1 and neighbour not in visited:
                queue.append(neighbour)
                visited.add(neighbour)
    
    return path


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


def bellman_ford(n, edges, src):
    dist = n * [float('inf')]
    dist[src] = 0

    for i in range(n - 1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            print("Negative cycle is detected")

    return dist



def floyd_warshall(graph):
    n = len(graph)
    dist = [row[:] for row in graph]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist



def prim(graph, start):
    total_weight = 0
    mst_edges = []
    min_heap = [(0, start, None )]
    visited = set()

    while min_heap:
        weight, current_node, from_node = heapq.heappop(min_heap)

        if current_node in visited:
            continue

        if from_node is not None:
            mst_edges.append((from_node, current_node, weight))
            total_weight += weight

        for neighbour, weight in graph[current_node]:
            if neighbour not in visited:
                heapq.heappush((weight, neighbour, current_node))
                visited.add(neighbour)
        
    return mst_edges, total_weight


def topsort(graph):
    visited = set()
    result = []
    for node in graph:
        if node not in visited:
            dfs(node, graph, visited, result)

    return result[::-1]

def dfs(node, graph, visited, result):
    if node in visited:
        return
    visited.add(node)
    for neighbour in graph[node]:
        dfs(neighbour, graph, visited, result)
    result.append(node)