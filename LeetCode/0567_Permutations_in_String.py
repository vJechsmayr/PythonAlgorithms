#Sliding Window Approach
from collections import Counter
class Solution:
    def checkInclusion(self, s1, s2):
        d1, d2 = Counter(s1), Counter(s2[:len(s1)])
        for start in range(len(s1), len(s2)):
            if d1 == d2: return True
            d2[s2[start]] += 1
            d2[s2[start-len(s1)]] -= 1
            if d2[s2[start-len(s1)]] == 0: 
                del d2[s2[start-len(s1)]]
        return d1 == d2