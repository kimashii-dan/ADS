class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        if not self.root:
            self.root = Node(val)
        else:
            self.insert2(self.root, val)

    def insert2(self, node, val):
        if node.val > val:
            if node.left is None:
                node.left = Node(val)
            else:
                self.insert2(node.left, val)
        else:
            if node.right is None:
                node.right = Node(val)
            else:
                self.insert2(node.right, val)


    def search(self, val):
        return self.search2(self.root, val)
    
    def search2(self, node, val):
        if node is None or node.val == val:
            return node
        elif node.val > val:
            return self.search2(node.left, val)
        else:
            return self.search2(node.right, val)
    
    def inorder(self, node, result):
        if node:
            self.inorder(node.left, result)
            result.append(node.val)
            self.inorder(node.right, result)

    def preorder(self, node, result):
        if node:
            result.append(node.val)
            self.preorder(node.left, result)
            self.preorder(node.right, result)

    def postorder(self, node, result):
        if node:
            self.postorder(node.left, result)
            self.postorder(node.right, result)
            result.append(node.val)


bst = BST()
bst.insert(5)
bst.insert(6)
bst.insert(2)
print(bst.search(2))