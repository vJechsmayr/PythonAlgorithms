# Author Aman Shekhar

def average(heights):
    heights = set(heights)
    return sum(heights) / len(heights)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
