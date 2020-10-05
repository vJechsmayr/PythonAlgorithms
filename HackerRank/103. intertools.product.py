# Author Aman Shekhar

from itertools import product

a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(*product(a, b))