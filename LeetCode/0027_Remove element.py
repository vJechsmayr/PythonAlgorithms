# Remove Element

"""
Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, 
you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example 1:

Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.

It doesn't matter what you leave beyond the returned length.
"""

import unittest


def removeElement(nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        for i in range(len(nums)):
            if nums[i] != val :
                nums[count] = nums[i]
                count +=1
        return count


# DO NOT TOUCH THE BELOW CODE


class RemoveElement(unittest.TestCase):
    def test_1(self):
        self.assertEqual(removeElement(
            [3,2,2,3],3), 2)



if __name__ == '__main__':
    unittest.main(verbosity=2)



        
    