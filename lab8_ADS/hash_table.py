hash_table = [[] for _ in range(10)]

print(hash_table)

def hash(value):
    sum = 0
    for char in value:
        sum += ord(char)
    return sum % 10

def add(value):
    index = hash(value)
    bucket = hash_table[index]
    if value not in bucket:
        bucket.append(value)

def contains(value):
    index = hash(value)
    bucket = hash_table[index]
    return value in bucket


names = ['Daniyar', 'Maksim', 'Anya', 'Lena', 'Anuar', 'Olzhas']

for name in names:
    add(name)

print(hash_table)