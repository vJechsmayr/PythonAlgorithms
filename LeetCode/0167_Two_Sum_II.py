# Problem name : Two Sum II - Input array is sorted
# Problem link : https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Contributor  : Herumb Shandilya

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for x in numbers:
            if x > target:
                break
            else:
                if target - x == x:
                    return (numbers.index(x)+1,numbers.index(x)+2)
                else:
                    if target - x in numbers:
                        return(numbers.index(x)+1,numbers.index(target - x)+1)