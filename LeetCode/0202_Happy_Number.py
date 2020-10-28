class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        checked = []
        while n != 1 and n not in checked:
            checked.append(n)
            n = sum([int(i) ** 2 for i in str(n)])
        if n == 1:
            return True
        return False