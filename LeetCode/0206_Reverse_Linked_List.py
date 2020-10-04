# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head, auxNode=None): #recursive mode
            if(head==None):
                return auxNode
            else:
                return self.reverseList(head.next, ListNode(head.val, auxNode))
            """
            :type head: ListNode
            :rtype: ListNode
            """