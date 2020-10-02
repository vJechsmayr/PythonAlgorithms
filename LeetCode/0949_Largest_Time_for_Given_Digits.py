import itertools
from typing import List

class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        """
        :type A: List[int]
        :rtype: str
        """
        result = ""
        for i in range(len(arr)):
            arr[i] *= -1
        arr.sort()
        for h1, h2, m1, m2 in itertools.permutations(arr):
            hours = -(10*h1 + h2)
            mins = -(10*m1 + m2)
            if 0 <= hours < 24 and 0 <= mins < 60:
                result = "{:02}:{:02}".format(hours, mins)
                break
        return result


print(Solution().largestTimeFromDigits([2,3,1,1]))