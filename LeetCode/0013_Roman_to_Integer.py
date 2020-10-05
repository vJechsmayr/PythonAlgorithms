def romanToInt(rom): 
	value = { 
		'M': 1000, 
		'D': 500, 
		'C': 100, 
		'L': 50, 
		'X': 10, 
		'V': 5, 
		'I': 1
	} 

	# Initialize previous character and answer 
	p = 0
	ans = 0
	
	# Traverse through all characters 
	n = len(rom) 
	for i in range(n-1, -1, -1): 

		# If greater than or equal to previous, 
		# add to answer 
		if value[rom[i]] >= p: 
			ans += value[rom[i]] 

		# If smaller than previous 
		else: 
			ans -= value[rom[i]] 

		# Update previous 
		p = value[rom[i]] 

	print(ans) 

romanToInt('MCMIV') 
