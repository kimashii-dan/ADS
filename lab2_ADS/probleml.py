class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
 
def findMaxSum(n: int, head: ListNode) -> int:
	max_sub = head.val
	cur_sum = 0
	cur = head
	while cur != None:
		if cur_sum < 0:
			cur_sum = 0
		cur_sum += cur.val
		max_sub = max(max_sub, cur_sum)
		cur = cur.next
	return max_sub
 
n = int(input())
a = list(map(int, input().split()))
head = ListNode(0)
tail = ListNode(0)
 
for i in range(n):
	tmp = ListNode(a[i])
	if i == 0:
		head = tmp
		tail = tmp
	else:
		tail.next = tmp
		tail = tmp
 
print(findMaxSum(n, head))