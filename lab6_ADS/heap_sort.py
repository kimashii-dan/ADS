import heapq

def min_merge_cost(arr):

    heapq.heapify(arr)
    n = len(arr)
    new_list = [0]*n
    for i in range(n):
        a = heapq.heappop(arr)
        new_list[i] = a

    return new_list


n = int(input())
values = [int(a) for a in input().split()[:n]] 

print(min_merge_cost(values))