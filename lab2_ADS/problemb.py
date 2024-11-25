class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.size = 0

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.size += 1

    def traverse(self):
        if self.head is None:
            print("List is empty!")
            return
        curr = self.head
        while True:
            print(curr.data, end=" ")
            curr = curr.next
            if curr == self.head:
                break
        print()

    def change_head(self, k):
        if self.head is None:
            print("List is empty!")
            return
        if k >= self.size or k < 0:
            print("Invalid shift")
            return
        for i in range(k):
            self.head = self.head.next

    

ayo = LinkedList()
n, k = map(int, input().split())
for s in map(str, input().split()[:n]):
    ayo.append(s)

ayo.change_head(k)
ayo.traverse()