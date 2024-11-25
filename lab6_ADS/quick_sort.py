
# def quick_sort(array):
#     length = len(array)

#     if length <= 1:
#         return array
#     else:
#         pivot = array.pop()
    
#     greater_items = []
#     smaller_items = []

#     for item in array:
#         if item > pivot:
#             greater_items.append(item)
#         else:
#             smaller_items.append(item)
    
#     return quick_sort(smaller_items) + [pivot]+ quick_sort(greater_items)


# print(quick_sort([1, 6, 4, 9, 3, 7, 10]))


def quick_sort(array, start, end):
    if end <= start:
        return
    pivot = partition(array, start, end)
    quick_sort(array, start, pivot - 1)
    quick_sort(array, pivot + 1, end)


def partition(array, start, end):
    pivot = array[end]
    i = start - 1
    for j in range(start, end):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
        
    i += 1
    array[i], array[end] = array[end], array[i]
    return i

array = [5, 2, 7, 6, 4, 3, 10, 8, 9]
quick_sort(array, 0, len(array) - 1)
print(array)