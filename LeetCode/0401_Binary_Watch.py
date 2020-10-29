class Solution(object):
    def combination(self, n, k, inp, res):
        # inp is expected to be a list of size n
        #print n,k,inp,res
        if k == 0:
            res.append([i for i in inp])
            return
        if k > n:
            return
        #for i in range(1,n+1):
        inp[n-1] = 1
        self.combination(n-1,k-1, inp, res)
        inp[n-1] = 0
        self.combination(n-1, k, inp, res)
            
        
    def getHours(self, h):
        if  h == 0:
            return ["0"]
        if h == 1:
            return ["1", "2", "4", "8"]
        if h == 2:
            return ["3", "5", "6", "9", "10"]
        if h == 3:
            return ["7", "11"]
        
    def getMinutes(self, m):
        inp = [0,0,0,0,0,0]
        res = []
        self.combination(6, m, inp, res)
        mins = [1, 2, 4, 8, 16, 32]
        minutes = []
        for comb in res:
            i = 0 
            mn = 0
            while i < 6:
                if comb[i] == 1:
                    mn += mins[i]
                i += 1
            if mn > 59:
                continue
            if mn < 10:
                minutes.append("0" + str(mn))
            else:
                minutes.append(str(mn))
        return minutes
        
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        i = 0
        res = []
        
        while i <= num:
            h = i
            m = num - i
            if h < 4 and m < 6:
                lh = self.getHours(h)
                #print lh
                lm = self.getMinutes(m)
                #print lm
                for hr in lh:
                    for mn in lm:
                        res.append(hr + ":" + mn)
            i += 1
        
        return res
