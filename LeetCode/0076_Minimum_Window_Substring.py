import collections


class Solution:
    def minWindow(self, s, t):

        count = collections.Counter(t)  # Statistics string The number of occurrences of characters in t
        miss = len(t)  # miss is responsible for recording whether the current window meets the conditions
        i = m = n = 0
        for j, v in enumerate(s, 1):  #Swipe right or expand
            miss -= (count[v] > 0)
            count[v] -= 1
            if not miss:  # Current window meets the condition
                while i < j and count[s[i]] < 0:  # 
                    count[s[i]] += 1
                    i += 1
                if not n or j-i <= n-m:  #Update new window
                    n, m = j, i
        return s[m:n]


if __name__ == '__main__':
    solu = Solution()
    s, t = 'ADOBECODEBANC', 'ABC'
    print(solu.minWindow(s, t))
