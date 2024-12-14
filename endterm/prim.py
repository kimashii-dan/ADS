import heapq

def prim_algorithm(graph, start_node):
    mst_edges = []
    total_weight = 0
    visited = set()
    min_heap = [(0, start_node, None)]

    while min_heap:
        weight, current_node, from_node = heapq.heappop(min_heap)

        if current_node in visited:
            continue

        visited.add(current_node)

        if from_node is not None:
            mst_edges.append((from_node, current_node, weight))
            total_weight += weight

        for neighbor, edge_weight in graph[current_node]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, neighbor, current_node))

    return mst_edges, total_weight

# Example usage
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 6)],
    'C': [('A', 4), ('B', 2), ('D', 3)],
    'D': [('B', 6), ('C', 3)]
}

start_node = 'A'
mst, total_weight = prim_algorithm(graph, start_node)
print("Minimum Spanning Tree:", mst)
print("Total Weight:", total_weight)