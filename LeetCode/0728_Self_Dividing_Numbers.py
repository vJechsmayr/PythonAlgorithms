class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for i in range(left, right+1):
            for char in str(i):
                if int(char)==0 or i % int(char)!=0:
                    break
            else:
                result.append(i)
        return result