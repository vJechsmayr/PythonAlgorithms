from collections import Counter
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        ans = 0
        c = Counter(nums)
        if k == 0:
            for val in c.values():
                if val > 1:
                    ans += 1
            return ans
        for i in c.keys():
            if i + k in c.keys():
                ans += 1
        return ans
