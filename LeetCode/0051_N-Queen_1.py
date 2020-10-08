# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 20:51:57 2020

@author: anjalisingh
"""

class Solution(object):
    def solveNQueens(self, n):
        # i is column index
        # left: left diagonal: \ level-i
        # right: right diagonal: / level+i
        self.col = [0]*n # not occupied column
        self.left = [0]*(2*n-1) # number of left diagonal
        self.right = [0]*(2*n-1)
        board = [['.' for x in range(n)] for y in range(n)]
        self.resultBoard = []
        self.backTrack(n, 0, board)
        return self.resultBoard

    def backTrack(self, n, level, board):
        if level == n: # finish
            res = []
            for i in range(n):
                res.append(''.join(board[i]))
            self.resultBoard.append(res)
            return
        for i in range(n): # iterate every column
            # if col, left, right are all not accupied, put a queue here
            if not self.col[i] and not self.left[level-i] and not self.right[level+i]:
                board[level][i] = 'Q'
                self.col[i] = 1
                self.left[level-i] = 1
                self.right[level+i] = 1 # choose
                self.backTrack(n, level+1, board) # explore
                board[level][i] = '.' # un choose
                self.col[i] = 0
                self.left[level-i] = 0
                self.right[level+i] = 0

# Queen  = Solution()
# print(Queen.solveNQueens(4))
