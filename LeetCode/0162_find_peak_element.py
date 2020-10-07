#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

'''

class Solution:

    def findPeak(self, nums):
        if not nums:
            return -1

        low, high = 0, len(nums) - 1
        while low <= high:
            if low == high:
                return low
            
            mid = (low + high)/2
            if nums[mid] < nums[mid + 1]:
                low = mid + 1
            else:
                high = mid
        
        return mid

    def findPeak1(self, nums):
        n = len(nums)
        if not nums:
            return -1
        peak = nums[0]
        for i in xrange(1, n -1):
            first = nums[i-1]
            mid = nums[i]
            last = nums[i+1]
            if first < mid > last:
                if peak < mid:
                    peak = mid
            else:
                i += 1
            
        if peak != nums[0]:
            return nums.index(peak)
        else:
            return -1

s = Solution()
A = [1,4,2,6,1]

print(s.findPeak(A))
print(s.findPeak1(A))