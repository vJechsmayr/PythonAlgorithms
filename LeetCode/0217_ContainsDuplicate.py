class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        noDup = set()
        for i in nums:
            if i in noDup:
                return True
            noDup.add(i)
        return False