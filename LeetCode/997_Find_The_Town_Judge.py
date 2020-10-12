class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        m=len(trust)
        if 1==N:
            if 0==m:
                return 1
        tmp={}
        dic={}
        for i in range(m):
            tmp[trust[i][0]]=1
        for i in range(m):
            if trust[i][1] not in tmp:
                if trust[i][1] not in dic:
                    dic[trust[i][1]]=1
                else:
                    dic[trust[i][1]]+=1
        for key in dic:
            if N-1==dic[key]:
                return key
        return -1
                
