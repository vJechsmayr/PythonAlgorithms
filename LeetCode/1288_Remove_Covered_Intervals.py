class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        inside = 0
        right = -1
        for i, j in intervals:
            if j <= right:
                inside += 1
            else:
                right = j
        return len(intervals) - inside
