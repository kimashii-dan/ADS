
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

def calc(s, k):
    l = len(s)
    p = build_LPS(s)
    return l + (l - p) * (k - 1)
    


t = int(input())

results = []
for i in range(t):
    s, k = input().split()
    results.append(calc(s, int(k)))


for result in results:
    print(result)