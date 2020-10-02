from collections import Counter
from functools import reduce
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        counted_elements = [Counter(s) for s in A]
        reduced_list = reduce(lambda x,y :x & y,counted_elements).elements() 
        return reduced_list