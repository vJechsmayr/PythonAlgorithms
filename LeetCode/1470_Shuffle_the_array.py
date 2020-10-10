class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        j = 0
        k = n
        for i in range(0, len(nums)):
            if i%2 == 0:
                ans.append(nums[j])
                j += 1
            else:
                ans.append(nums[k])
                k += 1
        return ans