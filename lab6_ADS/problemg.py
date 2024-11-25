def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


n = int(input())
nickname_map = {}
reverse_map = {}

for _ in range(n):
    old_nickname, new_nickname = input().split()

    if old_nickname in reverse_map:
        original_nickname = reverse_map[old_nickname]
    else:
        original_nickname = old_nickname

    nickname_map[original_nickname] = new_nickname
    reverse_map[new_nickname] = original_nickname

sorted_original_nicknames = quicksort(list(nickname_map.keys()))

print(len(sorted_original_nicknames))

for original_nickname in sorted_original_nicknames:
    print(original_nickname, nickname_map[original_nickname])
