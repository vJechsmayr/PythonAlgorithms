class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # using memoization technique

        # creating the list to track the minimum path
        mem = [item for item in triangle[-1]] # ---> array's nottom row is updated here

        # trying track backward from bottom-most array
        for i in range(len(triangle)-2, -1, -1): # ---> if len(triangle) = 5 -- range from 3, 2, 1 (in reverse order)
            for j in range(len(triangle[i])):
                mem[j] = triangle[i][j] + min(mem[j], mem[j+1]) # calculate the distance with minimum adjacent value

        #print (mem)
        return mem[0]
