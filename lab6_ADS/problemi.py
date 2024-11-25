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

lol = []
s = str(input())
for l in s:
    lol.append(l)

lol_sorted = quick_sort(lol)
for l in lol_sorted:
    print(l, end='')