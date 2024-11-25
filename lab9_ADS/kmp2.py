def build_lps(pattern):
    lps = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while (j > 0 and pattern[i] != pattern[j]):
            j = lps[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
    return lps

def kmp_search(text, pattern):
    combined = pattern + '#' + text
    lps = build_lps(combined)
    match_positions = []
    pattern_len = len(pattern)
    for i in range(len(pattern) + 1, len(combined)):
        if lps[i] == pattern_len:
            match_start = i - 2 * pattern_len
            match_positions.append(match_start)

    return match_positions


text = "ababcababcababc"
pattern = "ababc"
matches = kmp_search(text, pattern)
print("Pattern found at indices:", matches)
