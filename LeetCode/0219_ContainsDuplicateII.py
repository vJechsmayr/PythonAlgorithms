class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k < 1:
            return False
        seen = set()
        for i, n in enumerate(nums):
            if n in seen:
                return True
            if i >= k:
                seen.remove(nums[i-k])
            seen.add(n)
        return False
