def kmp_preprocess(pattern):
    m = len(pattern)
    lps = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
    return lps

def kmp_search(text, pattern, lps):
    n = len(text)
    m = len(pattern)
    j = 0
    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = lps[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == m:
            return True
    return False

def min_repetitions(A, B):
    m = len(B)

    lps = kmp_preprocess(B)

    repetitions = 0
    text = ""
    while len(text) < m:
        text += A
        repetitions += 1

    if kmp_search(text, B, lps):
        return repetitions
    elif kmp_search(text + A, B, lps):
        return repetitions + 1
    
    return -1

A = input().strip()
B = input().strip()
print(min_repetitions(A, B))
