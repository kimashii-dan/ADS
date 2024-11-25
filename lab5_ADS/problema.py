import heapq

def min_merge_cost(arr):

    heapq.heapify(arr)
    total_cost = 0

    while len(arr) > 1:
        first_min = heapq.heappop(arr)
        second_min = heapq.heappop(arr)
        merge_cost = first_min + second_min
        total_cost += merge_cost
        heapq.heappush(arr, merge_cost)
    
    return total_cost


n = int(input())
values = [int(a) for a in input().split()[:n]] 

print(min_merge_cost(values))