from typing import List

class Solution:
    def swap(self, list: List[int], a: int, b: int):
        list[a], list[b] = list[b], list[a]
        
    def removeElement(self, nums: List[int], val: int) -> int:
        startPointer = 0
        endPointer = len(nums) - 1

        while startPointer < endPointer:
            if nums[startPointer] == val:
                self.swap(nums, startPointer, endPointer)
                endPointer -= 1
            else:
                startPointer += 1
        
        return endPointer + 1
