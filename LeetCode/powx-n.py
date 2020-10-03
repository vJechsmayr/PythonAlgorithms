def power(x, n): 
  
    if (n == 0): return 1
    elif (int(n % 2) == 0): 
        return (power(x, int(n / 2)) *
               power(x, int(n / 2))) 
    else: 
        return (x * power(x, int(n / 2)) *
                   power(x, int(n / 2))) 
                   
x = int(input("Enter base : "))
n = int(input('Enter power : '))
print(power(x,n))

# Time Complexity : O(log(n))
#Soln by : 24Cipher
