#this program takes two integers and gives out a list of combinations

from itertools import combinations 
  
n=input("Enter the number till which you want the combinations")
k=input("Enter the length of the combinations")


numlist= []

for x in range (1, n):
    numlist.append(x)


comb = combinations(numlist,k) 
  
# Print the obtained combinations 
for i in list(comb): 
    print i