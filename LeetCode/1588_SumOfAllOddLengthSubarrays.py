class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        
        _sum = 0
        length = len(arr)
        sub_len = 1
        start = 0
        
        while sub_len <= length:
            for start in range(length - sub_len + 1):
                for i in range(start, start + sub_len):
                    _sum = _sum + arr[i]
            sub_len = sub_len + 2
            
        return _sum