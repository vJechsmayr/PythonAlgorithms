from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump_length_left = 0
        for num in nums:
            if jump_length_left == -1:
                return False
            jump_length_left = max(jump_length_left - 1, num - 1)

        return True
