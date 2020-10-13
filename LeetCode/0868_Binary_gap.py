def maxDist(n): 
	if (n == 0 or (n & (n - 1)) == 0): 
		return -1
	setBit = 1
	prev = 0
	i = 1
	while(i < 33): 
		prev += 1
		if ((n & setBit) == setBit): 
			setBit = setBit << 1
			break
		setBit = setBit << 1
	max0 = -10**9
	cur = prev 
	for j in range(i + 1, 33): 
		cur += 1
		if ((n & setBit) == setBit): 
			if (max0 < (cur - prev - 1)): 
				max0 = cur - prev - 1
			prev = cur 
		setBit = setBit << 1
	return max0 + 1

n = int(input())
print(maxDist(n)) 
