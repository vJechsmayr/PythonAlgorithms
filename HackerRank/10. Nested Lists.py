# Author Aman Shekhar

if __name__ == '__main__':
    student = {}

    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score in student:
            temp = student[score]
            temp.append(name)
            student[score] = temp
        else:
            temp = [name]
            student[score] = temp

    key = list(student.keys())
    key.sort()
    temp = list(student[key[1]])
    temp.sort()
    for i in temp:
        print(i)
