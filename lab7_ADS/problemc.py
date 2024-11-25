from collections import Counter

def find_common_elements(arr1, arr2):
    count1 = Counter(arr1)
    common_elements = []
    for num in arr2:
        if count1[num] > 0:
            common_elements.append(num)
            count1[num] -= 1

    return common_elements


n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
result = find_common_elements(arr1, arr2)
print(" ".join(map(str, result)))
