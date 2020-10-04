class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x > 0 and x < 10:
            return True

        copyNumber = x
        newNumber = 0
        while copyNumber > 0:
            newNumber = int(newNumber * 10 + (copyNumber % 10))
            copyNumber = int(copyNumber / 10)

        return newNumber == x