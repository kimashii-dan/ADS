def longest_common_substring(strings):
    def common_substring(s1, s2):
        m, n = len(s1), len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        longest = 0
        lcs_end = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    if dp[i][j] > longest:
                        longest = dp[i][j]
                        lcs_end = i
                else:
                    dp[i][j] = 0
        return s1[lcs_end - longest: lcs_end] if longest > 0 else ""
    common_substr = strings[0]
    for i in range(1, len(strings)):
        common_substr = common_substring(common_substr, strings[i])
        if not common_substr:
            break
    
    return common_substr

n = int(input())
strings = [input() for i in range(n)]


result = longest_common_substring(strings)
print(result)
