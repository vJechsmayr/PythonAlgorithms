'''
Problem: Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
'''
def MissingNumber(array):
    n = len(array)
    total = (n)*(n + 1)/2 # Series Sum: Length of the Array is [0, n] or N so sum of numbers from 0 -> N
    sumArray = sum(array) # Array Sum
    return total - sumArray # Find the difference between what series sum and the array sum - Yields the missing number
 
# Main - Ask for an array input from the user and print out the missing value
print("Please Enter The Elements One After The Other Separated By A Space In The Range [0, n] Omitting 1 Number:")
array = list(map(int,input().split()))
miss = MissingNumber(array)
print(f"The Missing Number From The Range Is: {miss}")
