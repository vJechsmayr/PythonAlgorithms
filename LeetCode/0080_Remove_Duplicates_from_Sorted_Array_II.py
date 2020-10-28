'''
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
'''


class Solution:
    # we want to leave at most two of each element
    def removeDuplicates(self, nums: list) -> int:
        length = 0
        lastNum = None
        lastLastNum = None

        # iterate in reverse order so that when we modify the list
        # it doesn't affect the order of the unvisited elements
        i = len(nums) - 1
        while i >= 0:
            el = nums[i]
            if el == lastLastNum:
                del nums[i]
            else:
                length += 1
            lastLastNum = lastNum
            lastNum = el
            i -= 1

        return length


if __name__ == '__main__':
    solution = Solution()
    input = [1, 1, 1, 2, 2, 3]
    solution.removeDuplicates(input)
    print(input)
    print(len(input))
