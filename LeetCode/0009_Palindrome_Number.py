class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        temp=x
        rev_num=0
        if(temp<0):
            return False
        while(temp):
            rem=temp%10
            rev_num=(rev_num*10)+rem
            temp=temp//10

        if rev_num==x:
            return True
        else:
            return False
        