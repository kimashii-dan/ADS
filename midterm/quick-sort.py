def quick_sort(array, start, end):
    if end <= start:
        return
    pivot = partition(array, start, end)
    quick_sort(array, start, pivot - 1)
    quick_sort(array, pivot + 1, end)


def partition(array, start, end):
    print(array)
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