class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.arr = []
        str1 = ""
        left,right = n,n
        self.kapa(str1,left ,right)
        return self.arr
    
    def kapa(self,current, left, right):
        if right:
            if left>0:
                string1 = current+"("
                self.kapa(string1, left-1, right)
            if left<right:
                self.kapa(current+")", left, right-1)
        else:
            self.arr.append(current)