class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for x in nums2:
            for y in range(len(nums1)):
                if nums1[y]==0:
                    nums1[y]+=x
                    break
        nums1.sort()
