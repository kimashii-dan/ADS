from collections import Counter

class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None
    
class linked_list:
    def __init__(self):
        self.head = node()
        self.tail = self.head
    
    def append(self, data):
        new_node = node(data)
        self.tail.next = new_node
        self.tail = new_node

    def traverse(self):
        if self.head is None:
            print("List is empty!")
            return
        cur = self.head
        elements = []
        while cur.next != None:
            cur = cur.next
            elements.append(cur.data)
        cnt = dict(Counter(elements))
        return cnt

ayo = linked_list()
n = int(input())
for a in [int(x) for x in input().split()[:n]]:
    ayo.append(a)

cnt = ayo.traverse()
max_value = max(cnt.values())

if max_value == 1:
    friends = [x for x in cnt.keys()]
    friends.sort(reverse = True)
    print(*friends)
else:
    keys_list = []
    for x, y in cnt.items():
        if y == max_value:
            keys_list.append(x)
    keys_list.sort(reverse = True)
    print(*keys_list)