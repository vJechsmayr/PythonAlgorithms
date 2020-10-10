class Solution:
    def __init__(self):
        pass

    def match(self,string,words,wordLen,n):
        wordsCopy = words.copy()
        Ind = 0
        for inds in range(n):
            subString = string[Ind:Ind + wordLen]
            if subString in wordsCopy :
                Ind += wordLen
                wordsCopy.remove(subString)
            else:
                return False
        return True

    def findSubstring(self,s, words): 
        Inds = []
        wordLen = len(words[0])
        n = len(words)
        sLen = len(s)
        for i in range(sLen):
            string = s[i:]
            if self.match(string,words,wordLen,n) == True:
                Inds.append(i)
        return Inds



