def rabin_karp(text, pattern, covered, base=256, prime=101):
    result = []
    n = len(text)
    m = len(pattern)
    pattern_hash = 0
    text_hash = 0
    h = 1

    for i in range(m - 1):
        h = (h * base) % prime

    for i in range(m):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % prime
        text_hash = (base * text_hash + ord(text[i])) % prime


    for i in range(n - m + 1):
        if pattern_hash == text_hash:
            if text[i:i + m] == pattern:
                for j in range(m):
                    covered[i + j] = True


        if i < n - m:
            text_hash = (base * (text_hash - ord(text[i]) * h) + ord(text[i + m])) % prime
            if text_hash < 0:
                text_hash += prime
    return covered


big_tape = str(input())
covered = [False] * len(big_tape)
n = int(input())
small_tapes = []
for i in range(n):
    a = str(input())
    small_tapes.append(a)

for small_tape in small_tapes:
    rabin_karp(big_tape, small_tape, covered)

no = False
for element in covered:
    if element == False:
        no = True
        break
    
if no:
    print('NO')
else:
    print('YES')


