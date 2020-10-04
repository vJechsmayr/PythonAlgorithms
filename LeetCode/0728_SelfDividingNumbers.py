class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        output = []
        for num in range(left,right+1):
            flag = 0
            L = [int(x) for x in str(num)]
            for j in L:
                if j == 0 or num%j != 0:
                    flag = 1
                    break
            if flag == 0:
                output.append(num)
                    
        return output