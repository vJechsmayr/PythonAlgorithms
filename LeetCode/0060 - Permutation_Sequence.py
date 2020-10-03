class Solution:
    data = []

    def getPermutation(self, n: int, k: int) -> str:
        string = []
        for i in range(1, n+1):
            string.append(str(i))
        self.permutations(string, 0, len(string))
        return self.data[k-1]

    def permutations(self, string, val, length):
        if val == length - 1:
            self.data.append("".join(string))
        else:
            for i in range(val, length):
                string[val], string[i] = string[i], string[val]
                self.permutations(string, val + 1, length)
                string[val], string[i] = string[i], string[val]


user = Solution()
output = user.getPermutation(int(input("Input: n=")), int(input("k=")))
print("\nOutput: {}".format(output))
