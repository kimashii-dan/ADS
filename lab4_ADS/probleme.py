class treeNode:
    def __init__(self, value=None):
        self.value = value
        self.right = None
        self.left = None

    def insert(self, value, parent, son):
        if self is None:
            treeNode(value)
            return 
        if self.value == parent:
            if son == 0:
                self.left = treeNode(value)
            else:
                self.right = treeNode(value)


            



