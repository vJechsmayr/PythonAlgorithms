class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        return '111' in "".join([str(i%2) for i in arr])