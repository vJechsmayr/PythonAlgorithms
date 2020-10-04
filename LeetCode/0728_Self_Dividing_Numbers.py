class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for i in range(left,right+1):
            include = True
            k = i
            while k:
                chk = k%10
                if not chk or i%chk != 0:
                    include = False
                    break
                k //= 10
            if include:
                res.append(i)
        return res

# Runtime: 32 ms, faster than 99.25% of Python3 online submissions for Self Dividing Numbers.