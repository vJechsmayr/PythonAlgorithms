'''Problem statement : Add binary
   Author:Ashvini More
   language :python3
'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        output = bin(int(a,2) + int(b,2))
        output = str(output).split('b')[1]
        return output