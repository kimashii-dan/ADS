class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    
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
        return elements

    def insert(self, index, data):
        if self.head is None:
            print("List is empty!")
            return
        cur = self.head
        new_node = node(data)
        count = 0
        while cur.next != None:
            if count == (index):
                new_node.next = cur.next
                cur.next = new_node
            cur = cur.next
            count += 1



ayo = linked_list()
n = int(input())
for i in range(n):
    a = int(input())
    ayo.append(a)

data = int(input())
index = int(input())
if n == index:
    ayo.append(data)
else:
    ayo.insert(index, data)

meow = ayo.traverse()
print(*meow)