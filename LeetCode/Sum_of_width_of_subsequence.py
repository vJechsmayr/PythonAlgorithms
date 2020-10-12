# Python3 implementation of above approach 

# Function to return sum of width of all subsets 
def SubseqWidths(A): 
	MOD = 10**9 + 7
	N = len(A) 
	A.sort() 

	pow2 = [1] 
	for i in range(1, N): 
		pow2.append(pow2[-1] * 2 % MOD) 

	ans = 0
	for i, x in enumerate(A): 
		ans = (ans + (pow2[i] - pow2[N - 1 - i]) * x) % MOD 
	return ans 


# Driver program 
n = int(input("Enter number of elements"))
#to convert input numbers into list of integers
A = list(map(int,input("enter the no. of elements").strip().split()))[:n] 

print(SubseqWidths(A)) 
