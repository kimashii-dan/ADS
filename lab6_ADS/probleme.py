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
    
    return quick_sort(greater_items)  + [pivot] + quick_sort(smaller_items)



def rows_to_cols(array, m):
    result = []
    for i in range(m):
        result.append([sub[i] for sub in array])
    return result

def cols_to_rows(array, n):
    result = []
    for i in range(n):
        result.append([sub[i] for sub in array])
    return result
    


n, m = map(int, input().split())
rows = []
for i in range(n):
    rows.append(list(map(int, input().split()[:m])))


cols = rows_to_cols(rows, m)
for i in range(len(cols)):
    sorted_cols = quick_sort(cols[i])
    cols[i] = sorted_cols
rows = rows_to_cols(cols, n)

for row in rows:
    for num in row:
        print(num, end=' ')
    print()