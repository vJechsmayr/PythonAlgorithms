class Solution(object):
    def prefixesDivBy5(self, A):
        """
        :type A: List[int]
        :rtype: List[bool]
        """
        prev = 0
        for i in range(len(A)):
            prev = 2 * prev + A[i]
            A[i] = prev % 5 == 0
        return A

