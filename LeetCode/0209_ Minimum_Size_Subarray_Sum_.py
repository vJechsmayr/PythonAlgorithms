class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """

        # approach:
        #     1. build a prefix list and iterate it
        #     2. at each iteration, use binary search to find prefix+s
        #     3. after search done, get length between left and i

        n = len(nums)
        result = n + 1

        if n == 0:
            return 0

        # build prefix sums array
        prefix = [0 for i in range(n+1)]
        for i in range(1, n+1):
            prefix[i] = prefix[i-1] + nums[i-1]

        # for each iteration i, we try to use binary search to find
        # prefix[i] + s, which means the sum of subarray between i
        # and left will be more than s
        for i in range(n):
            left = i + 1
            right = n
            target = prefix[i] + s

            while left <= right:
                m = left + (right - left) // 2

                if prefix[m] < target:
                    left = m + 1

                # in both greater and equal cases, we have to update
                # right index for finding the leftist sum which is
                # larger than target
                else:
                    right = m - 1

            # end for-loop immediately if left is greater than n because
            # it means every sum will be less than targer in following iteration
            if left > n:
                break

            # if left is valid, left will be the leftist element that is
            # larger than target, so length between left and i is what we need
            if left - i < result:
                result = left - i

        return 0 if result > n else result