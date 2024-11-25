from collections import deque
class treeNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):

        if value < self.value:
            if self.left is None:
                self.left = treeNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = treeNode(value)
            else:
                self.right.insert(value)
        
    def getHeight(self):
        if self is None:
            return 0
        left_height = self.left.getHeight() if self.left else 0
        right_height = self.right.getHeight() if self.right else 0
        return max(left_height, right_height) + 1
    
    def levelSums(self):
        if not self:
            return []
        
        result = []
        queue = deque([self])
        
        while queue:
            level_sum = 0
            level_size = len(queue)
            
            for i in range(level_size):
                node = queue.popleft()
                level_sum += node.value
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(level_sum)
        
        return result

n = int(input())

values = [int(a) for a in input().split()[:n]] 

root = None

for i in values:
    if root is None:
        root = treeNode(i)
    else:
        root.insert(i)

print(root.getHeight())
print(*root.levelSums())