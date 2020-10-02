class Solution:
    def jump(self, nums):
        if len(nums) == 1:
            return 0
        # number of jumps currently
        jump = 0
        # max index by current number of jumps
        cur = 0
        # max index by current + 1 number of jumps
        next = 0
        for i in range(len(nums)):
            if i > cur:
                jump += 1
                if cur == next:
                    return -1
                cur = next
            next = max(next, nums[i] + i)
        return jump
