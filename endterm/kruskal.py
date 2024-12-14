class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, vertex1, vertex2):
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)

        if root1 != root2:
            self.parent[root2] = root1

def kruskal(vertices, edges):
    edges.sort(key=lambda x: x[2])
    ds = DisjointSet(vertices)
    mst = []
    mst_weight = 0

    for u, v, weight in edges:
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst.append((u, v, weight))
            mst_weight += weight

    return mst, mst_weight

# Example usage
vertices = ['A', 'B', 'C', 'D']
edges = [
    ('A', 'B', 1),
    ('B', 'C', 4),
    ('A', 'C', 5),
    ('B', 'D', 2)
]

mst, mst_weight = kruskal(vertices, edges)
print("Minimum Spanning Tree:", mst)
print("Total weight:", mst_weight)
