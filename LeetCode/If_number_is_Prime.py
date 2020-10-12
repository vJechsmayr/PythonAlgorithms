# A optimized school method based 
# Python3 program to check 
# if a number is prime 


def isPrime(n) : 

	# Corner cases 
	if (n <= 1) : 
		return False
	if (n <= 3) : 
		return True

	# This is checked so that we can skip 
	# middle five numbers in below loop 
	if (n % 2 == 0 or n % 3 == 0) : 
		return False

	i = 5
	while(i * i <= n) : 
		if (n % i == 0 or n % (i + 2) == 0) : 
			return False
		i = i + 6

	return True


# Driver Program 
if (isPrime(11)) : 
	print(" true") 
else : 
	print(" false") 
	
if(isPrime(15)) : 
	print(" true") 
else : 
	print(" false") 
	
	
# This code is contributed 
# by Nikita Tiwari. 
