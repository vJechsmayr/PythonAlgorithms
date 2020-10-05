# Author Aman Shekhar

import numpy as np

n,m = map(int, input().split())
b = []
for i in range(n):
    a = list(map(int, input().split()))
    b.append(a)

b = np.array(b)

np.set_printoptions(legacy='1.13')
print(np.mean(b, axis = 1))
print(np.var(b, axis = 0))
print(np.std(b))