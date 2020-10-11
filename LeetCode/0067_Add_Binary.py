# Problem name : Add Binary
# Problem link : https://leetcode.com/problems/add-binary/
# Contributor  : Herumb Shandilya

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        l_a = [int(x) for x in list(a)]
        l_b = [int(x) for x in list(b)]
        num_a = sum([l_a[i]*(2**(len(l_a)-i-1)) for i in range(len(l_a))])
        num_b = sum([l_b[i]*(2**(len(l_b)-i-1)) for i in range(len(l_b))])
        s = num_a + num_b
        return bin(s)[2:]
