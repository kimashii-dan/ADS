import heapq

def main(values, k):
    values = [-value for value in values]
    heapq.heapify(values)
    total = 0
    for i in range(k):
        largest = -heapq.heappop(values)
        total += largest
        largest -= 1
        heapq.heappush(values,-largest)
    
    return total

n, k = map(int, input().split())
values = [int(a) for a in input().split()[:n]] 

print(main(values, k))



