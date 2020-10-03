# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:


        if head == None or head.next == None:
            return head
        count = 1
        p = head
        while p.next:
            count+=1
            p=p.next
            
        rot = k%count
        temp = head
        p.next = head
        for i in range(count-rot-1):
            temp = temp.next
        answer = temp.next
        temp.next = None
        
        return answer
        
        