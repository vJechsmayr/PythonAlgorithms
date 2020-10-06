class Solution:
    def romanToInt(self, s: str) -> int:
        self.s = s
        key = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,
'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        s = list(s)
        new = []
        for i in range(len(s)-1):
            try:
                n_s = "".join([s[i],s[i+1]])
            except: 
                break
            if n_s in ['IV','IX','XL','XC','CD','CM']:
                s[i] = n_s
                s.pop(i+1)
        for i in s:
            new.append(key.get(i))
        return sum(new)
                