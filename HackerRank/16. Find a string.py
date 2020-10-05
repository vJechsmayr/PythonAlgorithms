# Author Aman Shekhar

def count_substring(string, sub_string):
    count = 0
    for i in range(0, len(string) - len(sub_string) + 1):
        if string[i] == sub_string[0]:
            flag = 1
            for j in range(0, len(sub_string)):
                if string[i + j] != sub_string[j]:
                    flag = 0
                    break
            if flag == 1:
                count += 1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)