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
    
    def delete_evens(self):
        if self.head is None:
            print("List is empty!")
            return
        count = 0
        cur = self.head
        while True:
            if cur.next == None or cur.next.next == None:
                break
            cur = cur.next
            cur.next = cur.next.next


ayo = linked_list()
n = int(input())
for a in [int(x) for x in input().split()[:n]]:
    ayo.append(a)

ayo.delete_evens()
print(*ayo.traverse())