class Solution:
    def numDecodings(self, s: str) -> int:
        def in_range(n):
            if n[0] == '0':
                return False
            to_int = int(n)
            if to_int <= 26 and to_int > 0:
                return True
            return False
        
        N = len(s)
        a, b = 1, 1
        if N == 0 or s[0] == '0':
            return 0
        
        for i in range(1, N):
            extra = a if in_range(s[i-1:i+1]) else 0
            c = extra + (b if in_range(s[i]) else 0)
            a, b = b, c
        return b 
