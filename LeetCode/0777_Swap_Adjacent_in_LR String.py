# L can move left util L meets R. And R can move right util R meets L !! X is something that does not really need attention

class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        
        if start.replace('X', '') != end.replace('X', ''):
             return False

        m = collections.Counter()
        for s, e in zip(start, end):
            m[s] += 1
            m[e] -= 1
            if m['L'] > 0 or m['R'] < 0:
                return False
        return True