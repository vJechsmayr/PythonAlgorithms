class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        results = []
        def Combination(permutation, counter):
            if len(permutation) == len(nums):
                results.append(list(permutation))
                return

            for num in counter:
                if counter[num] > 0:
                    permutation.append(num)
                    counter[num] -= 1
                    Combination(permutation, counter)
                    permutation.pop()
                    counter[num] += 1

        Combination([], Counter(nums))

        return results