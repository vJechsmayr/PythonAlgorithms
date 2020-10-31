"""
Given an integer, write a function to determine if it is a power of three.

Example 1:

Input: 27
Output: true
Example 2:

Input: 0
Output: false
Example 3:

Input: 9
Output: true
Example 4:

Input: 45
Output: false
Follow up:
Could you do it without using any loop / recursion?
"""
class Solution(object):
    def isPowerOfThree(self, n):
        if n<1:
            return False
        elif n == 1:
            return True
        elif n == 2:
            return False
        else:
            while n > 2:
                a, b = divmod(n, 3)
                if b == 0:
                    n = a
                else:
                    break
        if n==1:
            return True
        else:
            return False
        
