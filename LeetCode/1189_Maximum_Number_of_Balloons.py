class Solution(object):
    def maxNumberOfBalloons(self, text) -> int:
        """
        :type text: str
        :rtype: int
        """
        a_count = text.count("b")
        b_count = text.count("a")
        l_count = text.count("l") / 2
        o_count = text.count("o") / 2
        n_count = text.count("n") 
        return int(min([a_count,b_count,l_count,o_count,n_count]))