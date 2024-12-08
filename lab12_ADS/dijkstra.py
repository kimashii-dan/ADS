import heapq

class WeightedGraph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node1, node2, weight):
        if node1 not in self.graph:
            self.graph[node1] = {}
        if node2 not in self.graph:
            self.graph[node2] = {}
        self.graph[node1][node2] = weight

    def display(self):
        for node, neighbors in self.graph.items():
            print(f"{node}: {neighbors}")

    def dijkstra(self, start):
        pq = []
        heapq.heappush(pq, (0, start))

        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0

        visited = set()

        while pq:
            current_distance, current_node = heapq.heappop(pq)

            if current_node in visited:
                continue

            visited.add(current_node)

            for neighbor, weight in self.graph.get(current_node).items():
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))

        return distances


graph = WeightedGraph()
n = int(input())
result = []
for i in range(n):
    node1, node2, weight = input().split()
    weight = int(weight)
    graph.add_edge(node1, node2, weight)

graph.display()

source = input()
distances = graph.dijkstra(source)
for node, distance in distances.items():
    print(f"Distance to {node}: {distance}")