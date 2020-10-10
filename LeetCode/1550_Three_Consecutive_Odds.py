class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        ok = False
        for i in range(0, len(arr) - 2):
            ok |=arr[i] & 1 and arr[i + 1] & 1 and arr[i + 2] & 1
        return ok
