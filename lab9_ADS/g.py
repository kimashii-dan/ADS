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

    return lps[-1]

def calc(s):
    n = len(s)
    maximum = build_LPS(s)
    minimum = n - maximum

    if (n % minimum) in range(0, minimum):
        return minimum
    else:
        return n
    
s = input()

print(calc(s))

# Input: bcabcab
# Output: 3

