#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 00:13:21 2020

@author: anjalisingh

Leet Code Accepted Code
"""

class Node:
    def __init__(self, val=None):
        self.val = val;
        self.next = None

class Solution:
    def __init__(self):
        self.head = None

    # def InsertAtBeg(self, d):
    #     nn = Node(d)
    #     nn.next = self.head
    #     self.head = nn



    # def Print(self):
    #     printVal = self.head
    #     while printVal is not None:
    #         print(printVal.val)
    #         printVal = printVal.next

    def reverseKGroup(self, head, k):
        cnt = 0
        c =0
        curr = head
        next = None
        prev = None
        temp = curr
        while temp is not None and c<k :
            temp = temp.next
            c = c + 1
        print(c)
        if c == k:
            while (curr is not None and cnt < k):
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
                cnt = cnt + 1

            if next is not None:
                head.next = self.reverseKGroup(next, k)
            return prev
        else:
            return curr

#     def ReverseNodeK(self, k):
#         self.head = self.reverseKGroup(self.head, k)




# LL = Solution()
# LL.InsertAtBeg(5)
# LL.InsertAtBeg(4)
# LL.InsertAtBeg(3)
# LL.InsertAtBeg(2)
# LL.InsertAtBeg(1)
# #LL.Print()
# LL.ReverseNodeK(3)
# LL.Print()
