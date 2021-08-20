class Solution:

    def rec(self, sinput, index, ans):
        n = len(sinput)
        if(index == n-1):
            ans.append(sinput.copy())
            return

        for i in range(index, n):
            sinput[i], sinput[index] = sinput[index], sinput[i]
            self.rec(sinput, index+1, ans)
            sinput[i], sinput[index] = sinput[index], sinput[i]

    def permute(self, nums):
        ans = []
        index = 0
        self.rec(nums, index, ans)
        return ans
