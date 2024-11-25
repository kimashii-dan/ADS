class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert_into_bst(root, value):
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = insert_into_bst(root.left, value)
    else:
        root.right = insert_into_bst(root.right, value)
    return root

def find_subtree(root, k):
    if root is None or root.value == k:
        return root
    if k < root.value:
        return find_subtree(root.left, k)
    else:
        return find_subtree(root.right, k)

def preorder_traversal(root, result):
    if root:
        result.append(root.value)
        preorder_traversal(root.left, result)
        preorder_traversal(root.right, result)


n = int(input())
gifts = list(map(int, input().split()))
k = int(input())


root = None
for gift in gifts:
    root = insert_into_bst(root, gift)


subtree_root = find_subtree(root, k)


result = []
preorder_traversal(subtree_root, result)


print(" ".join(map(str, result)))
