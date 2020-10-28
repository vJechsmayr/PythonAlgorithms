# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while head:
            if head.val == val:
                head = head.next
            else:
                break
        currentNode = head
        while currentNode:
            while currentNode.next and currentNode.next.val == val:
                currentNode.next = currentNode.next.next
            
            currentNode = currentNode.next
        return head
