from collections import Counter
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        n = len(secret)
        matched = []
        bulls = cows = 0
        for i in range(n):
            if secret[i] == guess[i]:
                bulls += 1
        
        a = Counter(secret)
        b = Counter(guess)
        
        for i in set(secret):
            cows += min(a[i], b[i])
        
        ans = str(bulls) + "A" + str(cows - bulls) + "B"
        return ans