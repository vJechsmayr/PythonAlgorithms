class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for _ in range(len(nums)-2):
            n = nums[i]
            if nums[i+2] != n:
                i += 1
                continue
            else:
                nums.pop(i+2)
                
        