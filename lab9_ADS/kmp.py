def KMP_search(text, pattern):
    lps = build_LPS(pattern)
    print(lps)
    i = 0
    j = 0
    n = len(text)
    m = len(pattern)
    matches = []
    
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
        
        if j == m:
            matches.append(i-j+1)
            j = lps[j - 1]
        
        elif i < n and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    
    return matches

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


text = input()
pattern = input()

matches = KMP_search(text, pattern)
print(len(matches))
print(*matches)