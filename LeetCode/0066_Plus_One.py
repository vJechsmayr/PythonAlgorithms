# Problem name : Plus One
# Problem link : https://leetcode.com/problems/plus-one/
# Contributor  : Shreeraksha R Aithal

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        i = -1
        carry = 1
        while i>=-n:
            digits[i] = digits[i] + carry
            carry = digits[i]//10
            digits[i] = digits[i]%10
            i = i-1
        
        if carry > 0:
            digits = [carry] + digits
        
        return digits