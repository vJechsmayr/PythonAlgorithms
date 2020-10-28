class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if points == []:
            return 0
        points.sort(key = lambda x: x[0])
        start = points[0][0]
        end = points[0][1]
        ans = len(points)
        for i in range(1, len(points)):
            if start <= points[i][0] <= end:
                ans -= 1
                if points[i][1] < end:
                    end = points[i][1]
            else:
                start = points[i][0]
                end = points[i][1]
                
        return ans
