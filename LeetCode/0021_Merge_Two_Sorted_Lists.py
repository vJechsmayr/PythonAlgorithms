# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        current_point = front = ListNode()

        while True:
            if l1 == None and l2 == None:
                break
            elif l1 == None:
                current_point.next = ListNode(l2.val)
                l2 = l2.next
            elif l2 == None:
                current_point.next = ListNode(l1.val)
                l1 = l1.next
            elif l1.val <= l2.val:
                current_point.next = ListNode(l1.val)
                l1 = l1.next
            else:
                current_point.next = ListNode(l2.val)
                l2 = l2.next
                    
            current_point = current_point.next
        
        return front.next
