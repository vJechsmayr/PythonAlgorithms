"""
213. House Robber II
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given a list of non-negative integers nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

This problem is solved using Dynamic Programming 
Time Complexity:- O(N)
Space Complexity: O(N) , we need to make 2 DP arrays so it takes O(2N) space

"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len( nums )
        # base conditions
        # if there is no element in array
        if n==0:
            return 0
        # if there is only one element in array return the element
        if n==1:
            return nums[0]
        # if there are 2 elements then return the max value out of both as we can't choose adjacent values together
        if n==2:
            return max(nums[0],nums[1])
        
      
        def max_profit(dp):
            """
            This function finds the max profit by robbing the adjacent houses using DP
            Input:- DP array of size n-1
            Output:- Max profit from that DP array
            """
            len_dp = len( dp )
            dp[1] = max( dp[0], dp[1] )
            for k in range( 2, len_dp ):
                dp[k] = max( dp[k - 1], dp[k] + dp[k - 2] )
    
            return dp[-1]

        """
        We exclude the last element in first case then find max profit 
        we exculde the first element in second case then find max profit
        we can't take both first and last element as they are adjacent 
        as last house is connected to first house
        """
        # find the profit excluding the last house
        dp_excludingLastElement = nums[:n - 1]
        profit1 = max_profit(dp_excludingLastElement)
        # find the profit using the first house
        dp_excludingFirstElement = nums[1:n]
        profit2 = max_profit(dp_excludingFirstElement)
        # return the max profit out of both the possibilites
        return max( profit1, profit2 )