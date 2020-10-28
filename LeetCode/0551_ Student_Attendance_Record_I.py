class Solution:
    def checkRecord(self, s: str) -> bool:
            aCount = 0;
            lCount = 0;
            for ch in s:
                if ch == "L":
                    lCount += 1
                else:
                    lCount = 0
                    
                if ch == "A":
                    aCount += 1
                    
                if lCount > 2:
                    return False
                if aCount > 1:
                    return False
                
            return True
            
