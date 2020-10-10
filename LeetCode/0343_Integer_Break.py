class Solution:
    def integerBreak(self, n: int) -> int:
        if n < 3:
            return 1
        if n == 3:
            return 2
        mylist = [1, 2, 3]
        for i in range(4, n+1):
            temp = [i]
            for j in range((i+1)//2):
                temp.append(mylist[j]*mylist[-j-1])
            mylist.append(max(temp))
            print(mylist, temp)
        return max(mylist)
    
solution = Solution()
print(solution.integerBreak(n =4))