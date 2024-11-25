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
        

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.value)
        if self.right:
            self.right.inorder()

    def find(self, value):
        if value < self.value:
            if self.left is None:
                return None
            else:
                return self.left.find(value)
        elif value > self.value:
            if self.right is None:
                return None
            else:
                return self.right.find(value)
        else:
            return self
    
    def find_subtree(self, value):
        node = self.find(value)
        if node is None:
            return "Value not found"
        else:
            return self.subtree_size(node)

    def subtree_size(self, node):
        if node is None:
                return 0
        left_branch = self.subtree_size(node.left)
        right_branch = self.subtree_size(node.right)
        return left_branch + right_branch + 1
        
    
        

n = int(input())

values = [int(a) for a in input().split()[:n]] 

root = None

for i in values:
    if root is None:
        root = treeNode(i)
    else:
        root.insert(i)

v = int(input())

print(root.find_subtree(v))