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


def common(unsorted_a1, unsorted_a2):
    a1 = quick_sort(unsorted_a1)
    a2 = quick_sort(unsorted_a2)
    common = []
    p1, p2 = 0, 0

    while p1 < len(a1) and p2 < len(a2):
        if a1[p1] == a2[p2]:
            common.append(a1[p1])
            p1 += 1
            p2 += 1
        elif a1[p1] < a2[p2]:
            p1 += 1
        else:
            p2 += 1
    return common


n, k = map(int, input().split())
if n > 0:
    person_1 = list(map(int, input().split()[:n]))
else:
    person_1 = []

if k > 0:
    person_2 = list(map(int, input().split()[:k]))
else:
    person_2 = []

print(*common(person_1, person_2))