# Definition for singly-linked list.
#class ListNode:
#    def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return head

        while (head.next is not None) and (head.val == head.next.val):
            while (head.next is not None) and (head.val == head.next.val):
                head = head.next
            head = head.next
            if head is None:
                return head
        
        head.next = self.deleteDuplicates(head.next)
        return head