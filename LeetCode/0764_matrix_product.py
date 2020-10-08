from functools import reduce
# matrix product using reduce, lambda
mat = [[1, 4, 5], [7, 3], [4], [46, 7, 3]] 
prod = reduce(lambda a,b:a*b, [j for i in mat for j in i])

print(prod)
