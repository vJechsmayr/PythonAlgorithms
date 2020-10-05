# Author Aman Shekhar

def merge_the_tools(string, k):
    # your code goes here

    temp = []
    len_temp = 0
    for item in string:
        len_temp += 1
        if item not in temp:
            temp.append(item)
        if len_temp == k:
            print(''.join(temp))
            temp = []
            len_temp = 0


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
