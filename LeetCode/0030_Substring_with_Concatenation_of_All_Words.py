
class Solution:

    def findSubstring(self,s, words):
        self.s = s
        self.words = words
        self.WordsLen = len(words[0])
        self.index = 0
        self.Leng = len(s)     
        self.output = []
        self.maxIndex = len(self.s) + 1 - self.WordsLen
        while self.index <= self.maxIndex :
            TempInd = self.index
            WordsCopy = self.words.copy()
            while TempInd <= self.maxIndex :
                tempStr = self.s[TempInd :TempInd + self.WordsLen]
                if tempStr in WordsCopy :
                    WordsCopy.remove(tempStr)
                    TempInd += self.WordsLen
                else:
                    break
            if WordsCopy == [] :
                print(self.index)
                self.output.append(self.index)
            self.index += 1
        return self.output

 
