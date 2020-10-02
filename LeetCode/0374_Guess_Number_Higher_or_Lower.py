class Solution(object):
    def guessNumber(self, n: int) -> int:
        """
        # The guess API is already defined.
        # @param num, your guess
        # @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
        # def guess(num: int) -> int:
        """
        low = 1
        high = n + 1
        mid = low + ((high - low)/2)
        res = guess(mid)
        while (res != 0):
            if res == 1:
                low = mid
            elif res == -1:
                high = mid
            mid = low + ((high - low)/2)
            res = guess(mid)
        return int(mid)
