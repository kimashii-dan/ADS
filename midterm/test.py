n = int(input())
values = [int(a) for a in input().split()[:n]] 
unique = set(values)
print(unique)  