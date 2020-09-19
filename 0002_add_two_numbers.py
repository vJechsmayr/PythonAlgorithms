
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
		r_tail = ListNode(0)
		r_head = r_tail
		carry = 0

		while l1 or l2 or carry:
			x = (l1.val if l1 else 0)
			y = (l2.val if l2 else 0)

			sum_ = x + y + carry
			carry = sum_//10

			new_node = ListNode(sum_ % 10)
			r_head.next = new_node
			r_head = new_node

			l1 = (l1.next if l1 else None)
			l2 = (l2.next if l2 else None)

		return r_tail.next

def main():
	n11 = ListNode(3)
	l1 = n11
	n12 = ListNode(4, l1)
	l1 = n12
	n13 = ListNode(2, l1)
	l1 = n13

	n21 = ListNode(4)
	l2 = n21
	n22 = ListNode(6, l2)
	l2 = n22
	n23 = ListNode(5, l2)
	l2 = n23

	resultLList = Solution().addTwoNumbers(l1, l2) 
	p = resultLList
	print("Result")
	while p:	
		print(p.val)
		p = p.next

if __name__ == "__main__":
	main()




