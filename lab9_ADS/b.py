def KMP_search(text, pattern):
    lps = build_LPS(pattern)
    i = 0
    j = 0
    n = len(text)
    m = len(pattern)
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
        
        if j == m:
            j = lps[j - 1]
        
        elif i < n and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
        
    return j

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

a = input()
b = input()
point = KMP_search(a, b)

if b[point:] + b[:point] == a:
    print(point)
else:
    print(-1)




# abcde
# decba