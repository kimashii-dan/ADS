def build_lps(pattern):
    lps = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while (j > 0 and pattern[i] != pattern[j]):
            j = lps[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
    return lps[-1]

prev_city = input()
n = int(input())
cities = []
for i in range(n):
    city = input()
    cities.append(city)


maximum = 0
results = []

for city in cities:
    combined = city + '#' + prev_city
    lps = build_lps(combined.lower())

    if lps > maximum:
        maximum = lps
        results = [city]
    elif lps == maximum and lps != 0:
        results.append(city)

print(len(results))
for city in results:
    print(city)
