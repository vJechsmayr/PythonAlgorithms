# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    '''
    Solution using Floyd's cycle-finding algorithm (tortoise and hare)
    '''

    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False

        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # If there is a cycle, fast will inevitably be on the same node as
            # slow.
            if fast is slow:
                return True
        return False


class SolutionO1:
    '''
    Solution to follow up. Disregards contents of each ListNode.
    '''

    def hasCycle(self, head: ListNode) -> bool:
        while head:
            if head.val is None:
                return True
            head.val = None
            head = head.next
        return False
