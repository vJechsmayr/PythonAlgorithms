class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n=len(nums)
        if n==0:
            return []
        dp=[[i,1] for i in range(n)]
        last=0
        maxm=0
        for i in range(1,n):
            for j in range(i-1,-1,-1):
                if nums[i]%nums[j]==0 and dp[j][1]>=dp[i][1]:
                    dp[i][1]=dp[j][1]+1
                    dp[i][0]=j
            if maxm<dp[i][1]:
                maxm=dp[i][1]
                last=i
        res=[]
        while dp[last][0]!=last:
            res.append(nums[last])
            last=dp[last][0]
        res.append(nums[last])
        res.reverse()
        return res
