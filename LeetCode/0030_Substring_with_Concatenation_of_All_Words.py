class Solution:

    def findSubstring(self,s, words):
        self.Incr = len(words[0])
        self.LenWords = len(words)
        self.Index = 0
        self.m = self.Incr * self.LenWords
        self.Max = len(s) - self.m
        self.output = []
        while self.Index <= self.Max :
            WordsCopy = words.copy()
            upperBound = self.Index
            lowerBound = upperBound + self.m
            for i in range(upperBound,lowerBound,self.Incr):
                tempStr = s[i: i + self.Incr]
                if tempStr in WordsCopy :
                    WordsCopy.remove(tempStr)
                else:
                    break
            if WordsCopy == [] :
                self.output.append(self.Index)
            self.Index += 1
        return self.output
        

                