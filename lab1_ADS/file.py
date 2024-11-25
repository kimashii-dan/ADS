# from collections import deque

# def initial_deck_order(n):
#     deck = deque()
#     for i in range(n, 0, -1):
#         deck.appendleft(i)
#         for i in range(i):
#             deck.appendleft(deck.pop())
#     return list(deck)


# t = int(input())
# results = []
# for i in range(t):
#     n = int(input())
#     results.append(" ".join(map(str, initial_deck_order(n))))
# print("\n".join(results))

from queue import Queue
from collections import deque

def print_queue(q):
    while not q.empty():
        print(q.get(), end=' ')
    print()

def reverse_queue(q):
    stack = []
    
    while not q.empty():
        stack.append(q.get())
        
    while stack:
        q.put(stack.pop())

def main():
    t = int(input())
    nums = [int(input()) for _ in range(t)]

    for n in nums:
        q = Queue()
        
        for j in range(n, 0, -1):
            q.put(j)
            for _ in range(j):
                el = q.get()
                q.put(el)

        reverse_queue(q)
        print_queue(q)

if __name__ == "__main__":
    main()




def check_string(s):
    result = []
    for char in s:
        if char == "#":
            if result:
                result.pop()
        else:
            result.append(char)
    return "".join(result)


x, y = [str(s) for s in input().split()]
if check_string(x) == check_string(y):
    print("Yes")
else:
    print("No")