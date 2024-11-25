# def hashcode(number):
#     length = len(number)
#     sum = 0
#     for i in range(length):
#         asc = ord(number[i])
#         sum += (asc - 47) * pow(11, i)
#     return str(sum % (pow(10, 9) + 7))

def hashcode(number):
    length = len(number)
    sum = 0
    MOD = 10**9 + 7
    for i in range(length):
        asc = ord(number[i])
        sum = (sum + (asc - 47) * pow(11, i, MOD)) % MOD
    return str(sum)


n = int(input())
hashmap = {}
for i in range(n * 2):
    key = str(input())
    hashmap[key] = hashcode(key)

for key, value in hashmap.items():
    if key not in hashmap.values():
        print(f'Hash of string "{key}" is {value}')

