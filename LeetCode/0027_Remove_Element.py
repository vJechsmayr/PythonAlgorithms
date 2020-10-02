class Solution(object):
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        :type nums: list
        :type val:  int
        :rtype: int (size of num)
        """
        while val in nums:
            nums.remove(val)
        return len(nums)
        
            