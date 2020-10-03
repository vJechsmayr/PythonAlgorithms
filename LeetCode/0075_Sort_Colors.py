# Problem name : Sort Colors
# Problem link : https://leetcode.com/problems/sort-colors/
# Contributor  : Shreeraksha R Aithal

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.        
        """
        
        i = k = 0
        n = len(nums)
        j = n-1
        while k < n and i < j:
            if nums[k] == 0:
                if k > i:
                    nums[i], nums[k] = nums[k], nums[i]
                    i += 1
                else:
                    k += 1
            elif nums[k] == 2:
                if k < j:
                    nums[j], nums[k] = nums[k], nums[j]
                    j -= 1
                else:
                    k += 1
            else:
                k += 1

