import heapq

def main(arr, k):

    heapq.heapify(arr)
    count = 0

    while arr[0] < k:
        if (len(arr) == 1):
            return -1
        first_min = heapq.heappop(arr)
        second_min = heapq.heappop(arr)
        new = first_min + 2 * second_min
        heapq.heappush(arr, new)
        count += 1
    
    return count


n, k = map(int, input().split())
values = [int(a) for a in input().split()[:n]] 

print(main(values, k))