# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def linkedListToInt(self, list_node, integer):
        integer += str(list_node.val)
        if list_node.next == None:
            return int(integer)
        else:
            return self.linkedListToInt(list_node.next, integer)

    def intToLinkedList(self, integer):
        integer = str(integer)
        print(integer)
        ll = [ListNode(int(integer[0]))]
        for i in range(1, len(integer)):
            ll.append(ListNode(int(integer[i])))
            ll[i - 1].next = ll[i]
        return ll[0]

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        first = self.linkedListToInt(l1, "")
        second = self.linkedListToInt(l2, "")
        summed = first + second
        return self.intToLinkedList(summed)
