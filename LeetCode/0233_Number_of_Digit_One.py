# Denote the number of 1 less than or equal to a given number
# Eg)
# Input: 13
# Output: 6 
# Explanation: Digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.

class Solution(object):
    def countDigitOne(self, n):
        number = 0
        i = 1 
        while(i <= n): 
            divider = i * 10
            number += (int(n / divider) * i +
                 min(max(n % divider -i + 
                              1, 0), i)) 
            i *= 10 
      
        return number