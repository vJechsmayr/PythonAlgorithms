# Author Aman Shekhar

for i in range(int(input())):
    a = int(input()); A = set(input().split())
    b = int(input()); B = set(input().split())
    print((A & B) == A)