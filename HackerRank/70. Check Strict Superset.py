# Author Aman Shekhar

A  = set(input().split())
n = int(input())
check = True
for i in range(n):
    s = set(input().split())
    if (s&A != s) or (s == A):
        check = False
        break
print(check)