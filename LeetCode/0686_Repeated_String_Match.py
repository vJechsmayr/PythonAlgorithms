class Solution(object):
    def repeatedStringMatch(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        # check for invalid inputs
        if (len(a) < 1) | (len(b) < 1) | (len(a) > 1e4) | (len(b) > 1e4):
            return -1

        # minimum repetitions of a for b to be a substring
        minRep = int(len(b)/len(a))
        rep = minRep
        
        # increment the number of repetitions at most twice (as in the worst case below)
        #           b b b b b b b b
        #       a a a-a a a-a a a-a a a
        while (rep <= min( minRep + 2, 1e4 )) and not (b in a*(rep)):
            rep += 1

        # The cycle exits when b is a substring of a repeated or if all the possible concatenations have been already checked
        # In the second case, the output is set to -1
        if not (b in a*(rep)):
            rep = -1

        return rep