# Author Aman Shekhar

from itertools import permutations
ip=input().split()
s=ip[0]
k=int(ip[1])
ans= list(permutations(s,k))
for i in sorted(ans):
    print ("".join(i))