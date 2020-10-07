import re

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        p = re.findall('[A-Z][^A-Z]*', pattern)
        result = []

        for x in queries:
            y = re.findall('[A-Z][^A-Z]*', x)
            if len(p) != len(y):
                result.append(False)
                
            else:
                q = []

                for i in range(len(p)):
                    t = 'false'
                    pi = p[i]
                    c = len(pi)
                    ct = 0

                    for j in y[i]:
                        if j == pi[ct]:
                            ct += 1
                        if ct == c:
                            t = 'true'
                            break
                    q.append(t)

                k = True
                if "false" in q:
                    k = False
                    
                result.append(k)
        return result
