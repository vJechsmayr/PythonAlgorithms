class Solution:
    def permuteUnique(self, nums):
        import itertools
        return list(set(itertools.permutations(nums)))