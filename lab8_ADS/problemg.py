def Rabin_Karp_Matcher(text, pattern, d=256, q=101):
    n = len(text)
    m = len(pattern)
    h = pow(d,m-1)%q
    p = 0
    t = 0
    result = []
    count = 0
    for i in range(m): # preprocessing
        p = (d*p+ord(pattern[i]))%q
        t = (d*t+ord(text[i]))%q
    for s in range(n-m+1): # note the +1
        if p == t: # check character by character
            match = True
            for i in range(m):
                if pattern[i] != text[s+i]:
                    match = False
                    break
            if match:
                result = result + [s]
                count += 1
        if s < n-m:
            t = (t-h*ord(text[s]))%q # remove letter s
            t = (t*d+ord(text[s+m]))%q # add letter s+m
            t = (t+q)%q # make sure that t >= 0
    return count


s = input().strip()
n = int(input())
result = []
for i in range(n):
    l, r = map(int, input().split())
    pattern = s[l-1:r]
    result.append(Rabin_Karp_Matcher(s, pattern))

for i in result:
    print(i)
