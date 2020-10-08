import math

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1:
            return s
        
        lenSec = numRows*2 - 2
        arr = ['' for i in range(numRows)]
        idy = 0
        
        for i in range(len(s)):
            iSeq = i % lenSec
            arr[idy] += s[i]
            
            if iSeq < numRows-1:
                idy += 1
            else:
                idy -= 1
                
        s_out = ''
        for i in arr:
            s_out += i
        
        return s_out