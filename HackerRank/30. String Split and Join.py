# Author Aman Shekhar

def split_and_join(line):
    # write your code here
    a = line.split( " ")
    a = "-".join(a)
    return a


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)