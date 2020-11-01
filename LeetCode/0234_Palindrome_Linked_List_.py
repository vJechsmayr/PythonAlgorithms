# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    
    def reverse(self, head):
        p = head.next
        while p and p.next:
            tmp = p.next
            p.next = p.next.next
            tmp.next = head.next
            head.next = tmp
            
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        #get middle pointer
        p1 = ListNode(0)
        p1.next = head
        p2 = p1
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
        
        # reverse second half of list
        self.reverse(p1)
        
        # check palindrome
        p1 = p1.next
        p2 = head
        while p1:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True