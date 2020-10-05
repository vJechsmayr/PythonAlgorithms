from itertools import permutations
class Solution:
    data = []

    def getPermutation(self, n: int, k: int) -> str:
        self.data = []
        string = []
        for i in range(1, n+1):
            string.append(str(i))
        string = list(permutations(string))
        temp = string[k-1]
        string = []
        string.append("".join(temp))
        return string[0]

   
