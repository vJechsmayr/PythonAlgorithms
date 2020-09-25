# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        final = 0
        output_listnode = ListNode() # To find the head of the list
        aux = output_listnode
        while (l1 is not None or l2 is not None) or final != 0:
            aux.next = ListNode()
            aux = aux.next
            if l1 is None:
                x = 0
            else:
                x = l1.val
                l1 = l1.next
            if l2 is None:
                y = 0
            else:
                y = l2.val
                l2 = l2.next
            final += (x + y)
            aux.val = final%10
            final = final//10
        
        return output_listnode.next