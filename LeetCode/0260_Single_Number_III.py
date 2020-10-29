class Solution:
    def singleNumber(self, N: List[int]) -> int:
    	L, d = len(N), set()
    	for n in N:
    		if n in d: d.remove(n)
    		else: d.add(n)
    	return d