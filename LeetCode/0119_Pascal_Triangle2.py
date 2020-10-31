class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        
        init = [1,1]
        for i in range(0, rowIndex-1):
            new_vec = []
            for v in range(0, len(init)-1):
                new_vec.append(init[v] + init[v+1])
            new_vec = [1] + new_vec + [1]
            init = new_vec
        return init
