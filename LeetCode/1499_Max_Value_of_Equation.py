class Solution(object):
    def findMaxValueOfEquation(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: int
        """
        ans = None

        d = deque()
        for x, y in points:
            while len(d) > 0 and d[0][0] < x - k:
                d.popleft()

            if len(d) != 0:
                ans = max(ans, x + y + d[0][1] - d[0][0])

            while (len(d) != 0) and d[-1][1] - d[-1][0] < y - x:
                d.pop()

            d.append((x, y))

        return ans
