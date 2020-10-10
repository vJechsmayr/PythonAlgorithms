import math

class Solution(object):
    def smallestGoodBase(self, n):
        """
        :type n: str
        :rtype: str
        """
        n = int(n)

        for length in range(64, 2, -1):
            l = 2
            r = int(math.sqrt(n) + 1)

            def sum(mid):
                res = 0
                for i in range(length - 1, -1, -1):
                    res += mid ** i
                    if res > n:
                        return res
                return res

            while l < r - 1:
                mid = (l + r) // 2
                if sum(mid) <= n:
                    l = mid
                else:
                    r = mid

            if sum(l) == n:
                return str(l)

        return str(n - 1)
