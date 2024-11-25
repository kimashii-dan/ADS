def build_LPS(pattern):
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


s = input()
lps= build_LPS(s)
count = 0
for i in range(1, len(lps)):
    if i % 2 == 0:
        k = i - lps[i - 1]
        if (i // k) % 2 == 0:
            count += 1

print(count)

