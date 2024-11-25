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
letters = [str(a) for a in input().split()[:n]]
pivot = str(input())
letters.append(pivot)

letters_sorted = quick_sort(letters)
letters_sorted = list(dict.fromkeys(letters_sorted))

pivot_index = letters_sorted.index(pivot)

if len(letters_sorted) == pivot_index + 1:
    answer = letters_sorted[0]
else:
    answer = letters_sorted[pivot_index + 1]

print(answer)