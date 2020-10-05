class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        sortList = sorted(set(nums))
        if len(sortList) > 2:
            num = sortList[-3]
        else:
            num = sortList[-1]
        return num
