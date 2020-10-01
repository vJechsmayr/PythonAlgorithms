  
  # Approach: Binary Search
  # Time Complexity: O(n) linear
  # Space Complexity: O(1) constant

class Solution(object):

    def searchRange(self, nums, target):
        l = self.search(nums, target, True)
        if l == -1:
            return [-1,-1]

        r = self.search(nums, target, False)
        return [l, r]

    def search(self, nums, target, isStart):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + int((right - left) / 2)
            if nums[mid] == target:
                if isStart:
                    if mid == 0:
                        return 0
                    else:
                        if nums[mid - 1] != target:
                            return mid
                        else:
                            right = mid - 1
                else:
                    if mid == len(nums) - 1:
                        return mid
                    else:
                        if nums[mid + 1] != target:
                            return mid
                        else:
                            left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1
