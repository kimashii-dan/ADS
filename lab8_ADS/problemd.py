def rabin_karp(text, pattern, base=256, prime=101):
    count = 0
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
                count += 1

        if i < n - m:
            text_hash = (base * (text_hash - ord(text[i]) * h) + ord(text[i + m])) % prime
            if text_hash < 0:
                text_hash += prime

    return count


results = {}
while True:
    n = int(input())
    if n == 0:
        break
    patterns = []
    for i in range(n):
        pattern = str(input())
        patterns.append(pattern)

    text = str(input())

    freq = {}
    for pattern in patterns:

        freq[pattern] = rabin_karp(text, pattern)


    maks = max(freq.values())
    dominating = [pattern for pattern in patterns if freq[pattern] == maks]

    results[maks] = dominating

for result in results:
    print(result)
    idk = results.get(result)
    for i in idk:
        print(i)



