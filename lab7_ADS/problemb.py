def merge_sorted_arrays(a, b):
    b.extend(a)
    b.sort()
    return b

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
result = merge_sorted_arrays(a, b)
print(" ".join(map(str, result)))
