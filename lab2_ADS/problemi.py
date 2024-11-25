class Node(object):
    def __init__(self, val=None, next=None, prev=None):
        self.val : int = val
        self.next: Node = next
        self.prev: Node = prev

results = []

def add_front(head: Node, node: Node) -> Node:
    node.next = head
    if head:
        head.prev = node
    results.append("ok" + "\n")
    return node

def add_back(head: Node, node: Node) -> Node:
    if head is None:
        results.append("ok\n")
        return node
    cur = head
    while cur.next:
        cur = cur.next
    cur.next = node
    node.prev = cur
    results.append("ok\n")
    return head

def erase_front(head: Node):
    if head is None:
        results.append("error\n")
        return head
    results.append(str(head.val) + "\n")
    return head.next if head.next else None

def erase_back(head: Node):
    if head is None:
        results.append("error" + "\n")
        return head
    if head.next is None:
        results.append(str(head.val) + "\n")
        return None
    cur = head
    while cur.next:
        cur = cur.next
    results.append(str(cur.val) + "\n")
    cur.prev.next = None
    return head

def front(head: Node):
    if head is None:
        results.append("error" + "\n")
    else:
        results.append(str(head.val) + "\n")
    return head

def back(head: Node):
    if head is None:
        results.append("error" + "\n")
        return head
    cur = head
    while cur.next:
        cur = cur.next
    results.append(str(cur.val) + "\n")
    return head

def clear(head: Node):
    results.append("ok\n")
    return None

def exit(head: Node):
    results.append("goodbye")
    return None
    
head: Node = None
while(True):
    vals = [str(i) for i in input().split()]
    if (vals[0] == "add_front"):
        head = add_front(head, Node(vals[1]))
    elif (vals[0] == "add_back"):
        head = add_back(head, Node(vals[1]))
    elif (vals[0] == "erase_front"):
        head = erase_front(head)
    elif (vals[0] == "erase_back"):
        head = erase_back(head)
    elif (vals[0] == "front"):
        head = front(head)
    elif (vals[0] == "back"):
        head = back(head)
    elif (vals[0] == "clear"):
        head = clear(head)
    elif (vals[0] == "exit"):
        head = exit(head)
        break

for result in results:
    print(result, end="")


# head = add_front(head, Node(0))
# head = add_front(head, Node(1))
# head = add_front(head, Node(1023))

# head = insert(head, Node(10), 0)
# head = insert(head, Node(34), 1)
# head = add_front(head, Node(24))
# head = add_front(head, Node(5))
# head = add_front(head, Node(32))
# head = add_back(head, Node(1))
# head = add_back(head, Node(2024))
# head = add_back(head, Node(548))

# head = erase_front(head)
# head = erase_back(head)

# head = front(head)
# head = back(head)

# head = clear(head)

# head = add_front(head, Node(23))
# head = add_front(head, Node(4))

# head = exit(head)
# printAll(head)