# Python3 program to print
# given matrix in spiral form
 
 
def spiralPrint(m, n, a):
    k = 0
    l = 0
 
    ''' k - starting row index
        m - ending row index
        l - starting column index
        n - ending column index
        i - iterator '''
 
    while (k < m and l < n):
 
        # Print the first row from
        # the remaining rows
        for i in range(l, n):
            print(a[k][i])
 
        k += 1
 
        # Print the last column from
        # the remaining columns
        for i in range(k, m):
            print(a[i][n - 1])
 
        n -= 1
 
        # Print the last row from
        # the remaining rows
        if (k < m):
 
            for i in range(n - 1, (l - 1), -1):
                print(a[m - 1][i])
 
            m -= 1
 
        # Print the first column from
        # the remaining columns
        if (l < n):
            for i in range(m - 1, k - 1, -1):
                print(a[i][l])
 
            l += 1
 
 
# Driver Code

R = int(input("Enter the number of rows:")) 
C = int(input("Enter the number of columns:")) 
  
# Initialize matrix 
matrix= [] 
print("Enter the entries rowwise:") 
  
# For user input 
for i in range(R):          # A for loop for row entries 
    a =[] 
    for j in range(C):      # A for loop for column entries 
         a.append(int(input())) 
    matrix.append(a) 

 
# Function Call
spiralPrint(R, C, matrix)
 
