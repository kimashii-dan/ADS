def sort_strings_by_length(sets):
    sorted_sets = []
    for s in sets:
        sorted_set = sorted(s, key=lambda x: (len(x), sets.index(s)))
        sorted_sets.append(" ".join(sorted_set))
    return "\n".join(sorted_sets)

T = int(input())
sets = [input().split() for _ in range(T)]
print(sort_strings_by_length(sets))
