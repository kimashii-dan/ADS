class Node(object):
    def __init__(self, val=0, next=None):
        self.val : int = val
        self.next: Node = next

def printAll(head: Node):
    cur = head
    result = []
    while cur:
        result.append(str(cur.val))
        cur = cur.next

    return " ".join(result) + "\n"

def insert(head: Node, node: Node, p: int) -> Node:
    if p == 0:
        node.next = head
        return node
    
    cur = head
    for i in range(p - 1):
        if cur is None:
            break
        cur = cur.next

    node.next = cur.next
    cur.next = node
    return head

def remove(head: Node, p: int):
    if head is None:
        return None
    
    if p == 0:
        return head.next
    
    cur = head
    for i in range(p - 1):
        cur = cur.next

    if cur.next is None:
        return head
    cur.next = cur.next.next
    return head

def replace(head: Node, p1: int, p2: int):
    if head is None:
        return None
    cur = head
    for i in range(p1):
        cur = cur.next
    head = remove(head, p1)
    head = insert(head, Node(cur.val), p2)
    return head

def reverse(head: Node):
    if head is None:
        return None
    cur = head
    prev = None
    while cur != None:
        next_node = cur.next
        cur.next = prev
        prev = cur
        cur = next_node    
    return prev
    
def cyclic_left(head: Node, x: int):
    if x == 0:
        return head
    if head is None:
        return None
    cur = head
    real_head = head
    for i in range(x):
        cur = cur.next
    temp = cur

    while cur.next != None:
        cur = cur.next
    cur.next = real_head

    while cur.next != temp:
        cur = cur.next
    cur.next = None 

    return temp


def cyclic_right(head: Node, x: int):
    if x == 0:
        return head
    cur = head
    size = 0
    while cur:
        cur = cur.next
        size += 1
    head = cyclic_left(head, size - x)
    return head

head: Node = None
results = []


while(True):
    vals = [int(i) for i in input().split()]
    if (vals[0] == 0):
        break
    elif (vals[0] == 1):
        head = insert(head, Node(vals[1]), vals[2])
    elif (vals[0] == 2):
        head = remove(head, vals[1])
    elif (vals[0] == 3):
        results.append(printAll(head))
    elif (vals[0] == 4):
        head = replace(head, vals[1], vals[2])
    elif (vals[0] == 5):
        head = reverse(head)
    elif (vals[0] == 6):
        head = cyclic_left(head, vals[1])
    elif (vals[0] == 7):
        head = cyclic_right(head, vals[1])


for result in results:
    print(result, end="")