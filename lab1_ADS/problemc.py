# def balance(s):
#     stack = []
#     for char in s:
#         if stack and char == stack[-1]:
#             stack.pop()
#         else:
#            stack.append(char)
    
#     return len(stack) == 0

# s = str(input())
# if balance(s):
#     print("YES")
# else:
#     print("NO")



# 1 3 5 7 9 - Boris
# 2 4 6 8 0 - Nursik

# 1 2
# 3 5 7 9 - Boris
# 4 6 8 0 1 2 - Nursik

# 3 4
# 5 7 9 - Boris
# 6 8 0 1 2 3 4 - Nursik

# 5 6
# 7 9 - Boris
# 8 0 1 2 3 4 5 6

# 7 8
# 9 - Boris
# 0 1 2 3 4 5 6 7 8

# 9 0
# [ ] - Boris
# 1 2 3 4 5 6 7 8 9 0 - Nursik

# Nursik wins in 5 moves.

# from collections import deque

# Boris = deque(int(n) for n in input().split())
# Nursik = deque(int(n) for n in input().split())

# count = 0
# max = 10**6
# while Boris and Nursik and count <= max:
#     boris_card = Boris.popleft()
#     nursik_card = Nursik.popleft()
#     if boris_card != nursik_card:
#         if boris_card == 0 and nursik_card == 9:
#             Boris.extend([boris_card, nursik_card])
#         elif boris_card == 9 and nursik_card == 0:
#             Nursik.extend([boris_card, nursik_card])
#         elif (boris_card > nursik_card):
#             Boris.extend([boris_card, nursik_card])
#         elif (boris_card < nursik_card):
#             Nursik.extend([boris_card, nursik_card])
#     count += 1

# if count > max:
#     print("blin nichya")
# elif not Boris:
#     print("Nursik", count)
# elif not Nursik:
#     print("Boris", count)

    



from collections import deque
deck = deque()
result = []
while True:
    elements = str(input()).split()
    if not elements:
        continue
    if elements[0] == "!":
        break
    if elements[0] == "*":
        if deck:
            if len(deck) == 1:
                total = deck[0] + deck[0]
                deck.pop()
            else:
                total = deck.pop() + deck.popleft()
            result.append(total)
        else:
            result.append("error")
    elif elements[0] == "+":
        deck.appendleft(int(elements[1]))
    elif elements[0] == "-":
        deck.append(int(elements[1]))

for r in result:
    print(r)
