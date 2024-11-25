
def string(n, hashes):
    result = []
    for i in range(n):
        if i == 0:
            char_val = hashes[i]
        else:
            char_val = hashes[i] - hashes[i - 1]

        char_code = (char_val // (2 ** i)) + 97
        result.append(chr(char_code))

    return result


n = int(input())
values = [int(a) for a in input().split()[:n]]

print(''.join(string(n, values)))