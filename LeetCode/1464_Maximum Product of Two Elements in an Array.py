class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        List.sort()

        max_product = (List[-1]-1) * (List[-2]-1)

        return max_product