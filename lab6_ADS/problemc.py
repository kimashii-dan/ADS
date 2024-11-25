def quick_sort(array):
    length = len(array)
    if length <= 1:
        return array
    else:
        pivot = array.pop()
    
    greater_items = []
    smaller_items = []
    for item in array:
        if item > pivot:
            greater_items.append(item)
        else:
            smaller_items.append(item)
    
    return quick_sort(smaller_items) + [pivot]+ quick_sort(greater_items)


n = int(input())
values = [int(a) for a in input().split()[:n]] 
sorted_values = quick_sort(values)

min_diff = float('inf')
n1, n2 = None, None
results = []
for i in range(n): 
    diff = abs(sorted_values[i] - sorted_values[i - 1])

    if diff == min_diff:
        results.append(sorted_values[i - 1])
        results.append(sorted_values[i])       

    if diff < min_diff:
        results = []
        min_diff = diff
        results.append(sorted_values[i - 1])
        results.append(sorted_values[i])

print(*results)