
# def calc(n, m):
#     if n == m:
#         return 0
    
#     diff = 0
#     operations = 0
#     computations = []


#     while n != m:
#         if n > m:
#             diff = abs(m - n)
#             computations.extend(range(n - 1, m - 1, -1))
#             n -= diff
#             operations += diff
        
#         if n < m:
#             n *= 2
#             operations += 1
#             computations.append(n)

#     return operations, computations
    
    
# n, m = map(int, input().split())
# answer = calc(n, m)
# if answer == 0:
#     print(answer)
# else:
#     print(answer[0])
#     print(*answer[1])

def min_operations(A, B):
    steps = []
    while A < B:
        steps.append(B)
        if B % 2 == 0:
            B //= 2
        else:
            B += 1

    while A > B:
        steps.append(B)
        B += 1
    
    steps.append(A)
    steps.reverse()
    print(len(steps) - 1)
    print(*steps[1:])

A, B = map(int, input().split())
min_operations(A, B)
