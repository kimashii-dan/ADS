def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    sorted = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted.append(left[i])
            i += 1
        else:
            sorted.append(right[j])
            j += 1

    sorted.extend(left[i:])
    sorted.extend(right[j:])
    
    return sorted

arr = [5, 2, 7, 6, 4, 3, 10, 8, 9]
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)
