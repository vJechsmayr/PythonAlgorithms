"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

def solve(head):
    d = {}
    h = head
    while(h):
        copy = Node(h.val)
        d[h] = copy
        h = h.next
    h = head
    while(h):
        copy = d[h]
        if(h.next):
            copy.next = d[h.next]
        if(h.random):
            copy.random = d[h.random]
        h = h.next
    if(head):
        return d[head]
    return None

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        return solve(head)
