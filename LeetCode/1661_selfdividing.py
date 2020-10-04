
# Function to check 
# the divisibility 
# of the number by 
# its digit. 
def checkDivisibility(n, digit) : 
	
	# If the digit divides the 
	# number then return true 
	# else return false. 
	return (digit != 0 and n % digit == 0) 
	
# Function to check if 
# all digits of n divide 
# it or not 
def allDigitsDivide( n) : 
	
	temp = n 
	while (temp > 0) : 
		
		# Taking the digit of 
		# the number into digit 
		# var. 
		digit = temp % 10
		if ((checkDivisibility(n, digit)) == False) : 
			return False

		temp = temp // 10
	
	return True

# Driver function 
n = 128 #true n=130 false

if (allDigitsDivide(n)) : 
	print("Yes") 
else : 
	print("No" ) 
	

