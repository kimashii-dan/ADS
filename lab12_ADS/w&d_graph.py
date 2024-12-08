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


graph = WeightedGraph()
n = int(input())
result = []
for i in range(n):
    node1, node2, weight = input().split()
    weight = int(weight)
    graph.add_edge(node1, node2, weight)

graph.display()
