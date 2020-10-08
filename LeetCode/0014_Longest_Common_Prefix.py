class Solution:
    #O(n)
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs)==0:
            return ''
        ans=''
        index=0
        for i in strs[0]:
            
            
            for j in range(len(strs)):
                
                y=strs[j]
                if index>=len(strs[j]) or i!=y[index]:
                    return ans
            
            ans+=i
            index+=1
        
        return ans