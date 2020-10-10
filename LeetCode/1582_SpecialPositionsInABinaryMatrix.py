class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        numSpecial = 0
        
        for a in range(len(mat)): 
            for b in range(len(mat[a])): 
                if mat[a][b] == 1:
                    valid = True
                    for c in range(len(mat[a])):
                        if mat[a][c] != 0 and c != b:
                            valid = False
                    if valid:
                        for d in range(len(mat)):
                            if mat[d][b] != 0 and d != a:
                                valid = False
                    if valid:
                        numSpecial+=1
        return numSpecial