# Author Aman Shekhar

for i in range(1, int(input())):  # More than 2 lines will result in 0 score. Do not leave a blank line also
    print(i * ((pow(10, i) - 1) // 9))