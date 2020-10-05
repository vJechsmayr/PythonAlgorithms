# Author Aman Shekhar

if __name__ == '__main__':
    arr = []
    l = []
    n = int(input())
    for _ in range(n):
        s = input().split()
        cmd = s[0]
        args = s[1:]
        if cmd !="print":
            cmd += "("+ ",".join(args) +")"
            eval("l."+cmd)
        else:
            print(l)
