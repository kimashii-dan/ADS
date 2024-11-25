# the idea is that user inputs number, for example 5 and loop goes 5 times through all prime numbers since the beginning. 

# prime numbers: 2 3 5 7 11 13 17 19 23 …

# 1 - 2
# 2 - 3
# 3 - 5
# 4 - 7
# 5 - 11


# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# def n_prime(n):
#     count = 0
#     num = 1
#     while count < n:
#         num = num + 1
#         if is_prime(num):
#             count = count + 1
#     return num

# n = int(input())
# print(n_prime(n_prime(n)))


# def is_prime(num):
#     if num <= 1:
#         return "NO"
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return "NO"
#     return "YES"

# n = int(input())
# print(is_prime(n))


from collections import deque

# def got_order(n):
#     deck = deque()
#     for i in range(n, 0, -1):
#         deck.appendleft(i)
#         for j in range(i):
#             deck.appendleft(deck.pop())
#     return deck
        

# meow = []
# t = int(input())
# for i in range(t):
#     n = int(input())
#     meow.append(got_order(n))

# for result in meow:
#     for digit in result:
#         print(digit, end=" ")
#     print()




t = int(input())
meow = []
for i in range(t):
    deck = deque()
    n = int(input())
    for i in range(n, 0, -1):
        deck.appendleft(i)
        for j in range(i):
            deck.appendleft(deck.pop())
    meow.append(deck)

for result in meow:
    for digit in result:
        print(digit, end=" ")
    print()
    