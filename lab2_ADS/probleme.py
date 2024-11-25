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

    def remove_duplicate(self):
        if self.head is None:
            print("list is empty")
            return
        cur = self.head
        while True:
            if cur.next == None:
                break
            if cur.data == cur.next.data:
                cur.next = cur.next.next
            else:
                cur = cur.next


ayo = linked_list()
n = int(input())
for i in range(n):
    i = str(input())
    ayo.append(i)

ayo.remove_duplicate()
meow = ayo.traverse()
meow.reverse()
print("All in all:", len(meow))
print("Students:")
for cat in meow:
    print(cat)