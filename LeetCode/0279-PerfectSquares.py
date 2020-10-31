class Solution(object):
    def numSquares(self, n):
        queue = collections.deque([(0, 0)])
        visited = set()
        while queue:
            val, dis = queue.popleft()
            if val == n:
                return dis
            for i in range(1, n+1):
                j = val + i*i
                if j > n:
                    break
                if j not in visited:
                    visited.add(j)
                    queue.append((j, dis+1))