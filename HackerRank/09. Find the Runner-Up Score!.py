# Author Aman Shekhar

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    x = set(arr)
    x = list(x)
    x.sort(reverse=True)
    print(x[1])
