class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Here we are using each element of list as keys, same can be achieved via set but that won't be ordered
        nums[:] = list(dict.fromkeys(nums))
        return len(nums)
        
            