'''
Problem:
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Solution:
Let k be the number of 2-steps taken
Then there are (n-2*k) 1-steps and k 2-steps to reach the top.
In total there are n/2 different k's for a given n, because then there are 0 1-steps and n/2 2-steps.
Using the binomial coeficcient the permutations of 1-steps and 2-steps for a given k can be calculated as
(n-(2*k)+k) choose k = (n-k) choose k
The total number of ways is thus
sum (n-k) choose k where k=0..n/2
The solution of this sum equals the (n+1)th fibonacci number as seen here: https://www.wolframalpha.com/input/?i=sum+%28n-k%29+choose+k+for+k%3D0..n%2F2
That way the problem becomes rather easy.
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        return self.fib(n + 1)

    fibStore = {}
    def fib(self, n: int) -> int:
        if n in self.fibStore:
            return self.fibStore[n]

        if n <= 2:
            return 1

        value = self.fib(n - 1) + self.fib(n - 2)
        self.fibStore[n] = value
        return value


print(Solution().climbStairs(30))
