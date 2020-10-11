def pushZerosToEnd(arr, n): 
    count = 0 
      
     
    for i in range(n): 
        if arr[i] != 0: 
              
            
            arr[count] = arr[i] 
            count+=1
      
    
    while count < n: 
        arr[count] = 0
        count += 1
          
# Driver code 
arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9] 
n = len(arr) 
pushZerosToEnd(arr, n) 
print("Array after pushing all zeros to end of array:") 
print(arr) 