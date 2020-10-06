class Solution:
    def romanToInt(self, s: str) -> int:
        
        symbolValDict = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        
        
        i = 0
        finalDigit = 0
        while(i<len(s)):
            firstDigit = symbolValDict[s[i]]
            if(i+1 < len(s)):
                nextDigit = symbolValDict[s[i+1]]
                if firstDigit >= nextDigit:
                    finalDigit += firstDigit
                    i+=1
                else:
                    finalDigit += nextDigit - firstDigit
                    i+=2
            else:
                finalDigit += firstDigit
                i+=1

            
        return finalDigit