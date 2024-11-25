import heapq


def main(values):
    values = [-value for value in values]
    heapq.heapify(values)

    while len(values) > 1:
        first_max = heapq.heappop(values)
        second_max = heapq.heappop(values)

        if (first_max != second_max):
            heapq.heappush(values, first_max - second_max)
    
    return -values[0] if values else 0



n = int(input())
values = [int(a) for a in input().split()[:n]] 

print(main(values))

