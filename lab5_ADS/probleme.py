import heapq

def main(values, a, k):
    if len(values) < k:
        heapq.heappush(values, a)
    else:
        heapq.heappushpop(values, a)


total = 0
values = []
results = []
n, k = map(int, input().split())
for i in range(n):
    c = input().strip()
    if c == "print":
        total = sum(values)
        results.append(total)
    else:
        a = int(c.split()[1])
        main(values, a, k)

for result in results:
    print(result)