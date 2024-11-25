n = int(input())
meow = []
for a in [int(x) for x in input().split()[:n]]:
    meow.append(a)
k = int(input())
min_diff = 0
pos = 0
for i in range(n):
    diff = abs(k - meow[i])
    if i == 0:
        min_diff = diff
    if min_diff > diff:
        min_diff = diff
        pos = i

print(pos)