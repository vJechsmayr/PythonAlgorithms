def rob(self, nums: List[int]) -> int:
  length = len(nums)
  if length == 0:
      return 0
  dp = [0] * len(nums)
  dp[0] = nums[0]
  for i in range(1,length):
      if i==1:
          dp[i] = max(dp[0],nums[i])
      elif i==2:
          dp[i] = dp[0]+nums[i]
      else:
          dp[i] = max(dp[i-2],dp[i-3]) + nums[i]
  return max(dp[length-1],dp[length-2])

'''
n = len(nums)
Time complexity = O(n)
Space complexity = O(n)
'''