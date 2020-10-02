# Import necessary dependencies
import sys

class Solution:
    def threeSumClosest(self, nums, target):
        # Sort the array
        nums.sort()
        # Initialize closest sum
        closest_sum = sys.maxsize

        # Starting from the first element,fix the smallest number
        # Implement the two pointers method in the remaining array
        for num in range(len(nums) - 2):
            # Initialize the two pointers
            # One pointing to the last element
            # the other pointing to element next to the fixed element.
            ptr_first, ptr_last = num + 1, len(nums) - 1

            # While the pointers don't cross each other
            while ptr_first < ptr_last:
                # Calculate the sum
                sum_temp = nums[num] + nums[ptr_first] + nums[ptr_last]

                # Compare against the variable closest_sum
                # If it is closer than the current closest_sum
                # Update closest sum. Also check :
                # If sum is greater than target, decrement ptr_last to decrease sum
                # Else, increment ptr_first to increase sum
                if abs(target - sum_temp) < abs(target - closest_sum):
                    closest_sum = sum_temp
                if sum_temp > target:
                    ptr_last = ptr_last - 1
                else:
                    ptr_first = ptr_first + 1
        return closest_sum
