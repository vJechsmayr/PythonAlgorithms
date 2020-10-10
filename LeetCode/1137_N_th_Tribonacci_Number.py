class Solution:
    def tribonacci(self, n: int) -> int:
        a, b, c = 0, 1, 1
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            for _ in range(n - 2):
                temp = a + b + c
                a = b
                b = c
                c = temp
            return temp
