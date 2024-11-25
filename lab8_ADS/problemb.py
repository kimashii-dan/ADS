def rabin_karp(text, pattern, base=256, prime=101):
    n = len(text)
    m = len(pattern)
    pattern_hash = 0
    text_hash = 0
    h = 1
    alignments = []

    for i in range(m - 1):
        h = (h * base) % prime

    for i in range(m):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % prime
        text_hash = (base * text_hash + ord(text[i])) % prime


    for i in range(n - m + 1):
        if pattern_hash == text_hash:
            if text[i:i + m] == pattern:
                alignments.append(i)

        if i < n - m:
            text_hash = (base * (text_hash - ord(text[i]) * h) + ord(text[i + m])) % prime
            if text_hash < 0:
                text_hash += prime

    return alignments


a = str(input())
b = str(input())
pattern = str(input())
student_1 = rabin_karp(a, pattern)
student_2 = rabin_karp(b, pattern)

count = 0
for i in student_1:
    if i in student_2:
        count += 1

print(count)

