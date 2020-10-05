# Author Aman Shekhar

n = input()
eng = set(map(int,input().split()))
b = input()
fre = set(map(int,input().split()))
print(len(eng.union(fre)))