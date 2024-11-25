from collections import deque
n = int(input())
s = str(input())

katsu = deque()
sakaya = deque()

for i in range(n):
    if s[i] == "K":
        katsu.append(i)
    else:
        sakaya.append(i)

while katsu and sakaya:
    k_index = katsu.popleft()
    s_index = sakaya.popleft()
    if k_index < s_index:
        katsu.append(k_index + n)
    else:
        sakaya.append(s_index + n)

if katsu:
    print("KATSURAGI")
else:
    print("SAKAYANAGI")