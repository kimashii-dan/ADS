class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class linked_list:
    def __init__(self):
        self.head = node()
    
    def append(self, data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node


    def find_nearest(self, k):
        cur = self.head
        count = 0
        diff = float('inf')
        pos = None
        while cur.next != None:
            cur = cur.next
            count += 1
            calc = abs(k - cur.data)
            if calc < diff:
                diff = calc
                pos = count
        return (pos - 1)
    
    
    
id_win = linked_list()
n = int(input())
for a in [int(x) for x in input().split()[:n]]:
    id_win.append2(a)
k = int(input())
print(id_win.find_nearest(k))


# 6
# 7 8 -10 4 2 -1
# 5

# 1: 7 - 5 = 2
# 2: 8 - 5 = 3
# 3: -10 - 5 = 15
# 4: 4 - 5 = 1
# 5: 2 - 5 = 3
# 6: -1 - 5 = 6

# The code is running too slow - O(n^2), loop in loop. So in order to optimize that we can append element and immediately calculate a difference.
        
            
    