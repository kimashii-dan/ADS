def distinct(s):
    MOD = 2**63 - 1
    BASE = 31
    
    n = len(s)
    result = set()
    for i in range(n):
        hash_value = 0
        power = 1
        for j in range(i, n):
            hash_value = (hash_value + (ord(s[j]) - ord('a') + 1) * power) % MOD
            power = (power * BASE) % MOD
            result.add(hash_value)
    
    return len(result)

s = input().strip()
print(distinct(s))

