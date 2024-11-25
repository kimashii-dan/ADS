from collections import deque, defaultdict

n, m, q = map(int, input().split())
red = set()
results = []
graph = defaultdict(list)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

queries = []
for i in range(q):
    a, b = map(int, input().split())
    queries.append((a, b))

for query in queries:
    print(query)

    first, second = query
    if first == 1:
        red.add(second)
    elif first == 2:
        if not red:
            results.append(-1)
            continue
        
        if second in red:
            results.append(0)
            continue

        visited = set()
        queue = deque([(second, 0)])
        visited.add(second)
        found = False
        while queue:
            current, distance = queue.popleft()
            print(current)
            if current in red:
                results.append(distance)
                found = True
                break

            for neighbor in graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, distance + 1))

        if not found:
            results.append(-1)

for res in results:
    print(res)

