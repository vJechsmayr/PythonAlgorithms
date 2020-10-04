class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for i in range(left,right+1):
            include = True
            k = i
            while k:
                chk = k%10
                if chk == 0 or i%chk != 0:
                    include = False
                    break
                k //= 10
            if include:
                res.append(i)
        return res

# Runtime: 40 ms, faster than 93.23% of Python3 online submissions for Self Dividing Numbers.