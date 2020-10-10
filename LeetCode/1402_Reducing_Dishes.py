class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        
        satisfaction.sort(reverse=True)
        ans = cur_sum = 0
        for ele in satisfaction:
            cur_sum += ele
            if cur_sum >= 0:
                ans += cur_sum
        
        return ans;