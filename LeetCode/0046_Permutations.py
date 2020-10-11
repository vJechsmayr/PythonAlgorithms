class Solution:
    def permutations(self, nums: List[int]):
        if not nums:
            yield []
        for num in nums:
            remaining = list(nums)
            remaining.remove(num)
            for perm in self.permutations(remaining):
                yield [num] + list(perm)
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(self.permutations(nums))
