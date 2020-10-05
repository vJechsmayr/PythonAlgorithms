# Author Aman Shekhar

import textwrap


def wrap(string, max_width):
    for i in range(0, len(string) + 1, max_width):
        result = string[i:i + max_width]
        if len(result) == max_width:
            print(result)
        else:
            return (result)


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
